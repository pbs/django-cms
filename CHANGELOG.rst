CHANGELOG
=========

Revision bbea94f (06.09.2018, 09:31 UTC)
----------------------------------------

No new issues.

* Misc commits

  * Pin pytest 3.4.0 and pytest-django 3.1.2

Revision 158aed6 (26.08.2016, 07:14 UTC)
----------------------------------------

No new issues.

* Misc commits

  * Pin html5lib.

Revision bbab8dd (06.05.2016, 15:16 UTC)
----------------------------------------

* LUN-2958

  * Rename plugin to component.
  * Replace plugin(s) with component(s)
  * Use componentsin cke plugins dropdown.

No other commits.

Revision e1d969c (11.04.2016, 08:03 UTC)
----------------------------------------

* LUN-2796

  * Add filter for dict.get().

* LUN-2956

  * fix embeded plugins edit buttons that have pk >= 1M

No other commits.

Revision 54fee0f (16.03.2016, 09:53 UTC)
----------------------------------------

* LUN-2890

  * Minor refactoring.
  * Provide hook to customize warnings when deleting plugins.

No other commits.

Revision 8edd04a (17.11.2015, 07:44 UTC)
----------------------------------------

* LUN-2595

  * show user display name for changed/created by fields

No other commits.

Revision bc1a2e0 (02.11.2015, 08:42 UTC)
----------------------------------------

* LUN-2483

  * Handle rendering disable case when cms toolbar is fully deactivated.

* LUN-2618

  * Order by descending change date.

* LUN-2661

  * fix negative margin on <body> when cms toolbar is present

No other commits.

Revision f01edc1 (23.10.2015, 13:06 UTC)
----------------------------------------

* LUN-2483

  * Added placeholder tag option to prevent rendering in edit mode.

* LUN-2727

  * Remove unnecessary checks.
  * rel.model in always Placeholder, rel.related_model must be checked.

* Misc commits

  * Remove unused import.
  * Use the ORM instead of a raw SQL.
  * Improve get of latest changed plugin.

Revision 583a604 (20.10.2015, 12:53 UTC)
----------------------------------------

* LUN-2702

  * Handle new exception thrown by django.contrib.sites.models.SiteManager

No other commits.

Revision e4f5460 (13.10.2015, 11:53 UTC)
----------------------------------------

* LUN-2507

  * Better assertion in test.
  * Prevent clashing urls generated from removing overwrite url.

* LUN-2594

  * Handle case when page id is not correct.

* LUN-2607

  * Check that the POST request does not perform actions that the user is not allowed.
  * Add attributes that the user does not have access to in hidden fields.
  * Remove unnecessary exclude. This is excluded in get_fieldsets.
  * Add test for case when writers change attributes that they cannot view/edit.

No other commits.

Revision bd0b5ad (01.10.2015, 12:20 UTC)
----------------------------------------

* LUN-2591

  * ordered sites list by name

* LUN-2592

  * chosen widget used on site selector

* Misc commits

  * Add migrations for cms and cms.plugins.link.

Revision ed1272d (23.09.2015, 15:12 UTC)
----------------------------------------

No new issues.

* Misc commits

  * Django 1.8: updated context for custom admin view
  * Django 1.8: updated templates
  * DJango 1.8 upgrade: removed some django1.9 deprecation warnings
  * Django1.8 upgrade: fixed deprecation warnings
  * Django1.8 upgrade: fixed deprecated code * fixed model permissions codenames * fixed returned data from get_deleted_objects * replaced TEMPLATE settings * fixed default_model_class for custom model related fields * fixed tests * pylinted some changed files

Revision 17b1187 (21.09.2015, 09:27 UTC)
----------------------------------------

* LUN-2632

  * apply ACE to copy page options modal

* Misc commits

  * Add missing migration for column description.

Revision 5bb3100 (11.09.2015, 13:55 UTC)
----------------------------------------

* LUN-2334

  * Rewrite relative import.
  * Changed cache deletion to improve performance.
  * Prevent cache clears during site deletion.
  * Rework for site data cache clear disabling.
  * Do not perform delete operations when it is not necessary.
  * Added option to disable and reenable cache clears.

* LUN-2583

  * removed preview from Text plugin
  * Removed preview

* LUN-2620

  * updated help-text for Template/Basic Settings
  * minor updates to Ace theme: preview in new tab

No other commits.

Revision 8f25086 (03.09.2015, 13:34 UTC)
----------------------------------------

* LUN-2282

  * update submit-row and buttons for all plugins according to Ace theme

* LUN-2283

  * css updates to match the Ace theme

* LUN-2460

  * pass plugin id directly into widget context
  * get plugin id from template instead of url
  * Resize iframe after CK Editor has been initialized

* LUN-2569

  * make entire header clickable for collapsing
  * 3: removed Note call from Page admin layout

* LUN-2596

  * left align fieldset fields

No other commits.

Revision 9494d2b (28.08.2015, 07:20 UTC)
----------------------------------------

* LUN-2310

  * updated if condition for tooltip to appear
  * error messages fix
  * fixed conflict with custom collapse.js
  * remaining of fieldset classes
  * error msgs styled
  * collapsible fieldsets updates
  * published labels updated + removed filters
  * title updates and resources ordering
  * breadcrumb updated

* Misc commits

  * Fix failing test - Rely on context['errors'] instead of checking for the presence of a css class to detect if an error occurred.

Revision f46db92 (06.08.2015, 13:40 UTC)
----------------------------------------

* LUN-2417

  * make pop-up window bigger for all plugins

* LUN-2503

  * Resolve decompress 500 error.

* LUN-2506

  * Remove validations so relative urls are allowed for the redirect and overwrite fields.

No other commits.

Revision 38d0bd2 (30.07.2015, 09:06 UTC)
----------------------------------------

* LUN-1966

  * Reverting stripping whitespaces
  * Fix for having query param site__exact point to a site where the user has no role

* LUN-2162

  * Set URL widget for the overwrite url field.
  * Increase width of CMS Page "Redirect" and "Overwrite URL" fields to match the width of the "Id" field.

* LUN-2418

  * Removed deprecated test and used exactly the same test from divio/django-cms.
  * Allow slug validation for existing pages with overwrite urls.
  * Fixed slug validation for newly created slugs.

* Misc commits

  * Fix docstring
  * Add test for cms.utils.get_available_slug infinite recursion
  * Fix COPY_SLUG_REGEX

Revision 4e3b183 (24.07.2015, 14:42 UTC)
----------------------------------------

* LUN-2467

  * fix CMS toolbar

* Misc commits

  * Fixed browser property for cms jquery
  * Django 1.7 upgrade: updated change form template from django
  * emergency fix for jstree

Revision f80e81f (17.07.2015, 10:45 UTC)
----------------------------------------

No new issues.

* Misc commits

  * disabled docs testcases; added sampleapp test templates
  * package should contain test templates in order for tests to run.
  * --pre allows django 1.8 prereleases installation
  * ignore db files generated by tests
  * Django 1.7 upgrade: fixed plugin name on add operation;
  * django 1.7 upgrade: fixed formfield overrides for page change form; fixed tox tests
  * Django 1.7 upgrade: fixed plugins table names; * made page field widget lazy * fixed tinymce json error
  * django 1.7 upgrade: tests run with pytest + some fixes
  * Django 1.7 upgrade: fixed errors, tests and deprecation warnings.
  * Django 1.7 upgrade: regen menus migrations
  * Django1.7 upgrade: regenerate migrations
  * Django 1.6 upgrade; fixed json import;
  * Django 1.6 upgrade: boolean field needs a default value
  * Django 1.6 upgrade * changed jquery-ui to 1.11.4 for compatibility with jquery 1.9.1
  * Django 1.6 upgrade: * fixed admin methods signatures * fixed page model form class * fixed django.conf.urls import * fixed json and truncate_chars import
  * Upgrade django 1.6: fixed adminmedia
  * fixed metaclasses
  * Django 1.5: replace import of simple_class_factory with lambda
  * remove obsolete verify_exists paramater from plugins.link.models.Link

Revision 203ba1e (03.07.2015, 08:43 UTC)
----------------------------------------

* LUN-2297

  * re-enable link plugin in ckeditor
  * remove unused code
  * no need for default ckeditor config
  * remove django-ckeditor use plain js ckeditor
  * CKEditor uses it's own jQuery, release it from global namespace
  * integrate CKEditor into CMS

No other commits.

Revision 1566109 (05.05.2015, 16:04 UTC)
----------------------------------------

No new issues.

* Misc commits

  * make page widget choices lazy

Revision 463467a (08.04.2015, 11:02 UTC)
----------------------------------------

* LUN-1919

  * Display site information on Change Page View

* Misc commits

  * django-cms-layouts tests fail because of django-cms 0.7.1

Revision 67e0d2b (03.03.2015, 12:36 UTC)
----------------------------------------

No new issues.

* Misc commits

  * mptt version upgrade

Revision fdd78c9 (17.02.2015, 10:33 UTC)
----------------------------------------

* LUN-2055

  * fixed double encoding when hitting cancel button

No other commits.

Revision 2e0b6f6 (06.02.2015, 13:17 UTC)
----------------------------------------

No new issues.

* Misc commits

  * small change
  * move page into closed/open page

Revision 182cafd (17.11.2014, 16:34 UTC)
----------------------------------------

No new issues.

* Misc commits

  * Update cms version
  * added some comments to make the code more explicit.
  * Added some tests for multiple sites permission issues
  * Users with pages permissions should always have access to admin pages section on the sites they have access to.
  * Pages changelist should always show items from an allowed working site.

Revision 842b35f (22.10.2014, 14:27 UTC)
----------------------------------------

* LUN-1912

  * Fix plugin editing icons position, disable editing when icons are visible

No other commits.

Revision 866ddbf (15.10.2014, 12:07 UTC)
----------------------------------------

* LUN-986

  * LUN-1608: Apply LUN-986 (make iframe embedable in text plugin)

* LUN-1608

  * fix tests
  * remove debug
  * move iframe_HTML_decode.py to cms templatetags folder, minor code refactor
  * ignore case when replacing
  * rename plugin controls styles id
  * minor code refactor
  * remove logging
  * Apply LUN-986 (make iframe embedable in text plugin)
  * add edit and delete plugin controlls in tinymce

No other commits.

Revision 4c4b59a (09.09.2014, 09:00 UTC)
----------------------------------------

* LUN-1452

  * Removed unnecessary path updates on move. Title paths are correctly updated on move for all cases (in page post save signal): * moved page becomes homepage * moved page was homepage before save * all descendants title paths are updated

* LUN-1832

  * fixed overwrite_url disappearance

* Misc commits

  * Update version as instructed by bamboo

Revision 4b5f557 (18.08.2014, 12:39 UTC)
----------------------------------------

* LUN-1371

  * Move the fix for LUN-1371 from django-robots to cms, where the fix seems to be more suitable due to the intrisic knowledge about cms internals.

No other commits.

Revision f62e66b (05.08.2014, 12:32 UTC)
----------------------------------------

No new issues.

* Misc commits

  * get_object_queryset should return a queryset without evaluation; This is a performance improvement(even with the extra query) that doesn't change the previous logic.

Revision c6668cc (08.07.2014, 11:31 UTC)
----------------------------------------

No new issues.

* Misc commits

  * Test moving home page down rewrites new home path.
  * pages should be cached only for sites that do not have pages in cache
  * fixed: page choices were always fetched from the databse even if they were in cache.
  * Update home only if the previous home was moved.
  * Save home to force removal of first slug.

Revision c975832 (03.07.2014, 07:43 UTC)
----------------------------------------

* LUN-1562

  * Made the 'table row' (in fact it's made with divs) in the cms pages admin view not to overlap

No other commits.

Revision 46802f2 (13.06.2014, 12:31 UTC)
----------------------------------------

* LUN-1596

  * Set callback to delete empty plugin image in text editor

* LUN-1633

  * page choices should be cached only for the sites that are in cache. Fixes the following problem: a site is created through the dbshell and the cache is not invalidated since the post save signals are not called.

No other commits.

Revision 6250c2b (30.05.2014, 10:50 UTC)
----------------------------------------

No new issues.

* Misc commits

  * Added tests for cache invalidation on page/site choices for page form field.
  * Pages choices are now cahced per site.
  * (tox) Fixed test results destination
  * Improved performance for fetching page field choices.
  * (tox) Added tox.ini

Revision 9c9ddef (17.04.2014, 13:11 UTC)
----------------------------------------

Changelog history starts here.
