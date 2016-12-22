$(document).ready(function () {
    // Handler for .ready() called.
    window.setTimeout(function () {
        location.href = "/";
    }, 5000);
    window.setInterval(function () {
        var valtime=parseInt($('.timeout .timeout-text-circle').text());
       $('.timeout .timeout-text-circle').text(valtime-1);
    }, 1000);
});