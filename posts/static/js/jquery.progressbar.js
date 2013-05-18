$.fn.progressbar = function(items){
  data = []
  for(i=0; i<items.length; i++){
    data[i] = $(items[i]).offset().top - window.innerHeight
  }

  // 进度条起始位置
  left = $(items[0]).width() + $(items[0]).offset().left + 60
  progressbar = this
  progressbar.css("left", left)

  change_progressbar = function (){
    curtop = document.body.scrollTop
    for(i=0; i<items.length; i++){
      if (curtop < data[i]) {
        break;
      };
    }
    $(".progressbar-bg").css("width", 150 * i / items.length)
    $(".progressbar-text").text("" + i + " / " + items.length)
  }

  $(window).scroll(change_progressbar)
  change_progressbar()
}