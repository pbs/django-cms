function CKEditorPlaceholderBridge(ckeditor) {
    this.ckeditor = ckeditor;

    
}

CKEditorPlaceholderBridge.prototype.insertText = function(text) {
    this.ckeditor.fire( 'saveSnapshot' );
    this.ckeditor.insertHtml(text);
    this.ckeditor.fire( 'saveSnapshot' );
};

CKEditorPlaceholderBridge.prototype.replaceContent = function(old, rep) {
    this.ckeditor.fire( 'saveSnapshot' );
    var body = this.ckeditor.document.getBody();
    var content = body.getHtml();
    content = content.split(old).join(rep);
    body.setHtml(content);
    this.ckeditor.fire( 'saveSnapshot' );
};

CKEditorPlaceholderBridge.prototype.selectedObject = function() {
    return this.ckeditor.getSelection().getSelectedElement();
};