$(function(){
    // 마크 다운
    $(".content-markdown").each(function(){
        var content = $(this).text()
        var markedContent = marked($.trim(content))
        $(this).html(markedContent)
    })
})