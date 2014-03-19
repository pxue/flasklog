$(document).ready(function(){

  $('.articles').fitVids();
  hljs.initHighlightingOnLoad();

  if ($("div#epiceditor").length > 0) {
    var opts = {
      container: 'epiceditor',
      textarea: 'content',
      basePath: '/static/css/',
      theme: {
        base: 'epiceditor.css',
        preview: 'style.css',
        editor: 'epic-dark.css'
      },
      autogrow: {
        minHeight: 350,
      },
      useNativeFullscreen: false,
      localStorageName: $('#permalink').val()
    };
    var editor = new EpicEditor(opts).load();
    var previewer = editor.getElement('previewer').body;
    $(previewer).wrap("<article></article>")
    $(previewer).wrap("<section class='articles'></section>")
    $(previewer).wrap("<div class='container'></div>")
  }


  //$('.flexslider').flexslider({
  //animation: "slide"
  //});
});
