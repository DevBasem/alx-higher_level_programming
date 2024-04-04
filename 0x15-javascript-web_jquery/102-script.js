$(document).ready(function () {
    $("#btn_translate").click(function () {
        let languageCode = $("#language_code").val();
        $.get(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`, function (data) {
            $("#hello").text(data.hello)
        });
    })
});
