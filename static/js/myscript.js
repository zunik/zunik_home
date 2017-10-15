$(function(){
    var $video_markdown = $(".video-md-convert div.video-md")

    if ($video_markdown.length > 0) {
         var video_before = "<div class='row justify-content-md-center'>" +
        "<div class='embed-responsive embed-responsive-16by9 col-md-6'>" +
        "<iframe class='embed-responsive-item' src='";

        var video_after = "' allowfullscreen></iframe></div></div>";

        $video_markdown.each(function () {
            var video_type = $(this).attr("data-type")
            var video_id = $(this).attr("data-id")

            if (video_type == 'youtube') {
                var query_string = '?rel=0'

                if ($(this).is('[data-start]')) {
                    query_string += '&start=' + $(this).attr("data-start")
                }

                if ($(this).is('[data-end]')) {
                    query_string += '&start=' + $(this).attr("data-end")
                }

                var video_src = "//www.youtube.com/embed/" + video_id + query_string;
            } else if (video_type == 'naver') {
                var video_key = $(this).attr("data-key")

                var video_src = "//serviceapi.rmcnmv.naver.com/flash/outKeyPlayer.nhn?vid=" + video_id + "&outKey=" + video_key + "&controlBarMovable=true&jsCallable=true&isAutoPlay=true&skinName=tvcast_white"
            }

            $(this).addClass("container mb-3");
            $(this).html(video_before + video_src + video_after)
        })
    }
})