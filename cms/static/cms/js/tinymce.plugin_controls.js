/* global edit_plugin */
//Add `edit` and `delete` controls for plugin placeholder inside text plugin
(function($){
    'use strict';
    $.fn.extend({
        getScreenPosition : function(ed){
            var parentWin = $(ed.getWin());

            return {
                top: this.get(0).offsetTop - parentWin.scrollTop(),
                left: this.get(0).offsetLeft - parentWin.scrollLeft()
            };
        }
    });

    function insertPluginControls(target, ed){
        if(!ed || !target){return;}

        var body = $(ed.getBody()),
            win = $(ed.getWin()),
            html = '',
            controls, edit, del;
        
        removePluginControls(ed);
        
        html += '<div class="plugin-controls">';
            html += '<div class="edit control"></div>';
            html += '<div class="delete control"></div>';
        html += '</div>';

        $(html).appendTo(body);
        controls = body.find('.plugin-controls');
        edit = controls.find('.edit');
        del = controls.find('.delete');

        controls.css(target.getScreenPosition(ed));
        controls.css({
            'width': target.width(),
            'height': target.height()
        });

        //placeholder image is too small to fit controls
        if(edit.outerWidth() + del.outerWidth() > target.width() ||
           edit.outerHeight() + del.outerHeight() > target.height()){
            controls.addClass('small');

            //even worse, the placeholedr is in the top left corner
            if(target.position().top - $(window).scrollTop() < edit.outerHeight()){
                controls.addClass('top');
            }

            //in case the placeholder is too close to the right edge
            if(del.outerWidth() + del.offset().left > body.width()){
                controls.addClass('right');
            }
        }

        del.click(function(){
            target.remove();
            removePluginControls(ed);
        });

        edit.click(function(){
            var taget_id_arr = target.attr('id').split('_'),
                obj_id = taget_id_arr[taget_id_arr.length - 1];

            // `edit_plugin` should be provided globally but worth to check
            if(typeof window.edit_plugin === 'function'){
                edit_plugin(obj_id);
            }
        });

        win.bind('scroll.'+ed.editorId, function(){
            controls.css(target.getScreenPosition(ed));
        });

        $('body').bind('click.'+ed.editorId, function(){
            removePluginControls(ed);
        });
    }

    function removePluginControls(ed){
        if(!ed){return;}

        $(ed.getBody()).find('.plugin-controls').remove();
        $(ed.getWin()).unbind('scroll.'+ed.editorId);
        $('body').unbind('click.'+ed.editorId);
    }

    tinymce.onAddEditor.add(function(mgr, ed){
        ed.onInit.add(function(ed){
            //append controls styles to editor iframe head
            $('#plugin-controls').appendTo($(ed.getDoc()).find('head'));
        });

        ed.onClick.add(function(ed, e){
            var targetId = e.target.id || '';

            if(targetId.match(/^plugin_obj_\d*$/)){
                insertPluginControls($(e.target), ed);
            }else{
                removePluginControls(ed);
            }
        });
    });

}(jQuery));