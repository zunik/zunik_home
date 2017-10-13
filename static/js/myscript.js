$(function(){
    var $youtube_markdown = $(".youtube-md div.youtube")

    if ($youtube_markdown.length > 0) {
         var youtube_start = "<div class='row justify-content-md-center'>" +
        "<div class='embed-responsive embed-responsive-16by9 col-md-6'>" +
        "<iframe class='embed-responsive-item' src='//www.youtube.com/embed/";

        var youtube_end = "' allowfullscreen></iframe></div></div>";

        $youtube_markdown.each(function () {
            var youtube_id = $(this).attr("data-id")

            var query_string = '?rel=0'

            if ($(this).is('[data-start]')) {
                query_string += '&start=' + $(this).attr("data-start")
            }

            if ($(this).is('[data-end]')) {
                query_string += '&end=' + $(this).attr("data-end")
            }

            $(this).removeClass("youtube").addClass("container mb-3");
            $(this).html(youtube_start + youtube_id + query_string + youtube_end)
        })
    }
})