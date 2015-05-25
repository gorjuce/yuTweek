$( document ).ready(function() {
    $('#addTweek #id_content').bind("keyup", function(){
        var max_characters = 140;
        var total_used = $("#id_content").val().length;
        var remaining = max_characters - total_used;
        $("#remaining").text(remaining);
    });
});