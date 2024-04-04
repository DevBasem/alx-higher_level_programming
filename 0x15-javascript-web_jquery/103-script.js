$(document).ready(function () {
    function getHelloTranslation() {
        let languageCode = $("#language_code").val();
        $.get(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`, function (data) {
            $("#hello").html(data.hello);
        });
    }

    $("#btn_translate").click(function () {
        getHelloTranslation();
    })

    $("#language_code").keypress(function(event) {
        if (event.keyCode === 13) {
            getHelloTranslation();
        }
    });
});
