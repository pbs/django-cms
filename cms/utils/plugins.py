# -*- coding: utf-8 -*-
from collections import namedtuple
from cms.exceptions import DuplicatePlaceholderWarning
from cms.models import Page
from cms.templatetags.cms_tags import Placeholder
from cms.utils.placeholder import validate_placeholder_name
from django.contrib.sites.models import Site
from django.shortcuts import get_object_or_404
from django.template.base import (
    NodeList, TextNode, VariableNode, TemplateSyntaxError, Variable)
from django.template.loader import get_template
from django.template.loader_tags import (
    IncludeNode, ExtendsNode, BlockNode)
import warnings

try:
    from sekizai.helpers import get_varname, is_variable_extend_node, engines
except ImportError:
    from sekizai.helpers import get_varname, is_variable_extend_node
    engines = None


def get_page_from_plugin_or_404(cms_plugin):
    return get_object_or_404(Page, placeholders=cms_plugin.placeholder)


def _extend_blocks(extend_node, blocks):
    """
    Extends the dictionary `blocks` with *new* blocks in the parent node (recursive)
    """
    # we don't support variable extensions
    if is_variable_extend_node(extend_node):
        return
    parent = extend_node.get_parent(get_context())
    # Search for new blocks
    for node in _get_nodelist(parent).get_nodes_by_type(BlockNode):
        if node.name not in blocks:
            blocks[node.name] = node
        else:
            # set this node as the super node (for {{ block.super }})
            block = blocks[node.name]
            seen_supers = []
            while hasattr(block.super, 'nodelist') and block.super not in seen_supers:
                seen_supers.append(block.super)
                block = block.super
            block.super = node
    # search for further ExtendsNodes
    for node in _get_nodelist(parent).get_nodes_by_type(ExtendsNode):
        _extend_blocks(node, blocks)
        break


def _find_topmost_template(extend_node):
    parent_template = extend_node.get_parent(get_context())
    for node in _get_nodelist(parent_template).get_nodes_by_type(ExtendsNode):
        # Their can only be one extend block in a template, otherwise django raises an exception
        return _find_topmost_template(node)
    # No ExtendsNode
    return extend_node.get_parent(get_context())


def _extend_nodelist(extend_node):
    """
    Returns a list of placeholders found in the parent template(s) of this
    ExtendsNode
    """
    # we don't support variable extensions
    if is_variable_extend_node(extend_node):
        return []
    blocks = extend_node.blocks
    _extend_blocks(extend_node, blocks)
    placeholders = []

    for block in blocks.values():
        placeholders += _scan_placeholders(_get_nodelist(block), block, blocks.keys())

    # Scan topmost template for placeholder outside of blocks
    parent_template = _find_topmost_template(extend_node)
    placeholders += _scan_placeholders(_get_nodelist(parent_template), None, blocks.keys())
    return placeholders


def _get_nodelist(tpl):
    if hasattr(tpl, 'template'):
        return tpl.template.nodelist
    else:
        return tpl.nodelist


def get_context():
    if engines is not None:
        return namedtuple('Context', 'template')(
            namedtuple('Template', 'engine')(engines.all()[0])
        )
    else:
        return {}


def _scan_placeholders(nodelist, current_block=None, ignore_blocks=None):
    placeholders = []
    if ignore_blocks is None:
        ignore_blocks = []

    for node in nodelist:
        # check if this is a placeholder first
        if isinstance(node, Placeholder):
            placeholders.append(node.get_name())
        # if it's a Constant Include Node ({% include "template_name.html" %})
        # scan the child template
        elif isinstance(node, IncludeNode):
            # if there's an error in the to-be-included template, node.template becomes None
            if node.template:
                # This is required for Django 1.7 but works on older version too
                # Check if it quacks like a template object, if not
                # presume is a template path and get the object out of it
                if not callable(getattr(node.template, 'render', None)):
                    # If it's a variable there is no way to expand it at this stage so we
                    # need to skip it
                    if isinstance(node.template.var, Variable):
                        continue
                    else:
                        template = get_template(node.template.var)
                else:
                    template = node.template
                placeholders += _scan_placeholders(_get_nodelist(template), current_block)
        # handle {% extends ... %} tags
        elif isinstance(node, ExtendsNode):
            placeholders += _extend_nodelist(node)
        # in block nodes we have to scan for super blocks
        elif isinstance(node, VariableNode) and current_block:
            if node.filter_expression.token == 'block.super':
                if not hasattr(current_block.super, 'nodelist'):
                    raise TemplateSyntaxError("Cannot render block.super for blocks without a parent.")
                placeholders += _scan_placeholders(_get_nodelist(current_block.super), current_block.super)
        # ignore nested blocks which are already handled
        elif isinstance(node, BlockNode) and node.name in ignore_blocks:
            continue
        # if the node has the newly introduced 'child_nodelists' attribute, scan
        # those attributes for nodelists and recurse them
        elif hasattr(node, 'child_nodelists'):
            for nodelist_name in node.child_nodelists:
                if hasattr(node, nodelist_name):
                    subnodelist = getattr(node, nodelist_name)
                    if isinstance(subnodelist, NodeList):
                        if isinstance(node, BlockNode):
                            current_block = node
                        placeholders += _scan_placeholders(subnodelist, current_block, ignore_blocks)
        # else just scan the node for nodelist instance attributes
        else:
            for attr in dir(node):
                obj = getattr(node, attr)
                if isinstance(obj, NodeList):
                    if isinstance(node, BlockNode):
                        current_block = node
                    placeholders += _scan_placeholders(obj, current_block, ignore_blocks)
    return placeholders

def get_placeholders(template):
    compiled_template = get_template(template)
    placeholders = _scan_placeholders(compiled_template.template.nodelist)
    clean_placeholders = []
    for placeholder in placeholders:
        if placeholder in clean_placeholders:
            warnings.warn("Duplicate placeholder found: `%s`" % placeholder, DuplicatePlaceholderWarning)
        else:
            validate_placeholder_name(placeholder)
            clean_placeholders.append(placeholder)
    return clean_placeholders

SITE_VAR = "site__exact"

def current_site(request):
    if SITE_VAR in request.REQUEST:
        return Site.objects.get(pk=request.REQUEST[SITE_VAR])
    else:
        site_pk = request.session.get('cms_admin_site', None)
        if site_pk:
            try:
                return Site.objects.get(pk=site_pk)
            except Site.DoesNotExist:
                return None
        else:
            return Site.objects.get_current()
