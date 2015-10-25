
/**
 * Created by wuda on 15/8/2.
 */




$("#publish_form").markdown({
  savable:true,
  onShow: function(e){
    alert("Showing "
      +e.$textarea.prop("tagName").toLowerCase()
      +"#"
      +e.$textarea.attr("id")
      +" as Markdown Editor...")
  },
  onPreview: function(e) {
    var previewContent
      alert("hello")

    if (e.isDirty()) {
      var originalContent = e.getContent()

      previewContent = "Prepended text here..."
             + "\n"
             + originalContent
             + "\n"
             +"Apended text here..."
    } else {
      previewContent = "Default content"
    }

    return previewContent
  },
  onSave: function(e) {
    alert("Saving '"+e.getContent()+"'...")
  },
  onChange: function(e){
    console.log("Changed!")
  },
  onFocus: function(e) {
    alert("Focus triggered!")
  },
  onBlur: function(e) {
    alert("Blur triggered!")
  }
})
