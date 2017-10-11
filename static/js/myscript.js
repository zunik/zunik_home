$(function(){
    var $youtube_markdown = $(".youtube-md div.youtube")

    if ($youtube_markdown.length > 0) {
         var youtube_start = "<div class='row justify-content-md-center'>" +
        "<div class='embed-responsive embed-responsive-16by9 col-md-6'>" +
        "<iframe class='embed-responsive-item' src='//www.youtube.com/embed/";

        var youtube_end = "?rel=0' allowfullscreen></iframe></div></div>";

        $youtube_markdown.each(function () {
            var youtube_id = $(this).attr("data-id")
            $(this).removeClass("youtube").addClass("container mb-3");
            $(this).html(youtube_start + youtube_id + youtube_end)
        })
    }
})