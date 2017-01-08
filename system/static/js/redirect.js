$(document).ready(function () {
    window.setInterval(function () {
        var valtime = parseInt($('.timeout .timeout-text-circle').text());
        $('.timeout .timeout-text-circle').text(valtime - 1);
        if (valtime-2 < 0) {
            location.href = "/";
        }
    }, 1000);
});