{% load i18n %}

function escapeHtml(html) {
    return html.replace(/&/g,"&amp;")
        .replace(/\"/g,"&quot;")
        .replace(/</g,"&lt;")
        .replace(/>/g,"&gt;");
}


function add_plugin(type, parent_id, language){
	$.post("add-plugin/", {
		parent_id: parent_id,
		plugin_type: type
	}, function(data) {
		if ('error' != data) {
			// Successfully created, data is pk of object, but object
			// is 'blank'. We now want to show the edit popup.

			// We only want to insert the text if the user actually
			// *saved* the object.  We don't have modal dialogs, so we
			// register a callback against the id number.  This callback
			// is called by dismissEditPluginPopup().
			var plugin_id = data;
			edit_plugin(plugin_id);
			editPluginPopupCallbacks[data] = function(plugin_id, icon_src, icon_alt){
                texteditor = get_editor("{{ name }}");
				texteditor.insertText(plugin_admin_html(plugin_id, icon_src, icon_alt));
				editPluginPopupCallbacks[data] = null; // Unbind callback
			};

		}
	}, "html");
}

function edit_plugin(obj_id) {
    editPluginPopupCallbacks[obj_id] = function(plugin_id, icon_src, icon_alt){
        var texteditor = get_editor("{{ name }}");
		var rExp = new RegExp('<img[^>]* id="plugin_obj_' + obj_id + '"[^>]*>', "g");
		try {
			texteditor.replaceContent(rExp, plugin_admin_html(plugin_id, icon_src, icon_alt));
		} catch (e) {}
		editPluginPopupCallbacks[obj_id] = null; // Unbind callback
	};


	// Pop up window for editing object.
    var newWin = window.open("edit-plugin/" + obj_id + "/?_popup=1",
                "Edit_plugin_object" + obj_id,
                "menubar=no,titlebar=no,toolbar=no,resizable=yes"
                  + ",width=800,height=300,top=0,left=0,scrollbars=yes"
                  + ",location=no"
               );
    if (!newWin) {
        alert('Your popup blocker is preventing the plugin editor.');
    }
}

function plugin_admin_html(plugin_id, icon_src, icon_alt) {
    return '<img src="' + escapeHtml(icon_src) + '" ' +
        'alt="'+ escapeHtml(icon_alt) + '" ' +
        'title="'+ escapeHtml(icon_alt) + '" ' +
        'id="plugin_obj_' + plugin_id + '"/>';
}


// Global function, needed for popup window to call the parent via opener.dismissEditPluginPopup
function dismissEditPluginPopup(win, plugin_id, icon_src, icon_alt) {
    // This is called after user presses 'Save' in popup.
    win.close();
    var callback = editPluginPopupCallbacks[plugin_id];
    if (callback != null) {
        callback(plugin_id, icon_src, icon_alt);
    }
}

/* General functions */
function get_editor(placeholder) {
    // Find the placeholder text editor widget
    if (typeof(PlaceholderEditorRegistry) == "undefined") {
        // This could occur if javascript defining PlaceholderEditorRegistry
        // has not been loaded for some reason.
        alert("{% filter escapejs %}{% trans "A programming error occurred - cannot find text editor widgets." %}{% endfilter %}");
        return null;
    }
    return PlaceholderEditorRegistry.retrieveEditor(placeholder);
}


function insertPluginControls($target, $body, $window, options){
    if(!$target){ return;}
    var $ = django.jQuery || jQuery;
    $.fn.extend({
        getScreenPosition : function(){
            return {
                top: (this.get(0).offsetTop - $($window).scrollTop()) + 'px',
                left: (this.get(0).offsetLeft - $($window).scrollLeft()) + 'px'
            };
        }
    });

    var controls = $('<div class="plugin-controls"></div>')
                        .append('<link rel="stylesheet" type="text/css" href="'+options.css+'">')
    controls.append('<div class="edit control"></div>');
    controls.append('<div class="delete control"></div>');
    controls.css($($target).getScreenPosition());

    $($window)[$.fn.on ? 'off' : 'unbind']('scroll');
    $($window)[$.fn.on ? 'on' : 'bind']('scroll', function(){
        controls.css($($target).getScreenPosition());
    });

    controls.css({
        'width': $($target).width(),
        'height': $($target).height()
    });

    controls = options.append($("<div />").append(controls.clone()).html());
    var controlsWH = 70;

    //placeholder image is too small to fit controls
    if(2 * controlsWH > $($target).width() ||
       2 * controlsWH > $($target).height()){
        controls.addClass('small');

        //even worse, the placeholedr is in the top left corner
        if($target.position().top < controlsWH){
            controls.addClass('top');
        }

        //in case the placeholder is too close to the right edge
        if(controlsWH + $($target).offset().left > $($body).width()){
            controls.addClass('right');
        }
    }
}