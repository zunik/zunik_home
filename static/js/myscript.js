$(function(){
    var $embed_markdown = $(".embed-md-convert div.embed-md")

    if ($embed_markdown.length > 0) {
        var embed_before = "<div class='row justify-content-md-center'><div class='embed-responsive embed-responsive-";
        var embed_before2 = " col-md-8'><iframe class='embed-responsive-item' src='";
        var embed_after = "' allowfullscreen></iframe></div></div>";

        // size 21by9, 16by9, 4by3, 1by1

        $embed_markdown.each(function () {
            var embed_type = $(this).attr("data-type")
            var embed_id = $(this).attr("data-id")
            var embed_size = '16by9'

            if (embed_type == 'youtube') {
                var query_string = '?rel=0'

                if ($(this).is('[data-start]')) {
                    query_string += '&start=' + $(this).attr("data-start")
                }

                if ($(this).is('[data-end]')) {
                    query_string += '&end=' + $(this).attr("data-end")
                }

                var embed_src = "//www.youtube.com/embed/" + embed_id + query_string;
            } else if (embed_type == 'naver') {
                var embed_key = $(this).attr("data-key")

                var embed_src = "//serviceapi.rmcnmv.naver.com/flash/outKeyPlayer.nhn?vid=" + embed_id + "&outKey=" + embed_key + "&controlBarMovable=true&jsCallable=true&isAutoPlay=true&skinName=tvcast_white"
            } else if (embed_type == 'sound_cloud') {
                embed_size = '4by3'

                var embed_src = "//w.soundcloud.com/player/?url=https%3A//api.soundcloud.com/tracks/" + embed_id +
                    "&amp;color=%230066cc&amp;auto_play=false&amp;hide_related=false&amp;show_comments=true&amp;show_user=true&amp;show_reposts=false&amp;show_teaser=true&amp;visual=true"
            }

            $(this).addClass("container mb-3");
            $(this).html(embed_before + embed_size + embed_before2 + embed_src + embed_after)
        })
    }

    // diary list 에 표현되는 content 에서는 링크 작동이 안되게
    $(".diary-list-view-content").find("a").removeAttr("href").addClass('a-tag-disable')
})