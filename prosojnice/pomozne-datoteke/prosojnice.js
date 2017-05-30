$(document).ready(function() { 

  $(".spoiler").hide();
  
  $('<a class="reveal">???</a>').insertBefore('.spoiler');

  $("a.reveal").click(function(){
    $(this).next().show();
    $(this).hide();
  });

}); 

var slideshow = remark.create({
  highlightLines: true
});
