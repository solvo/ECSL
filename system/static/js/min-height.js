$(document).ready(function () {
    var height_screen = $(window).height();
    var height_nav = $('header nav').height();
    var height_footer = $('footer').height();
    var height_container = height_screen - height_footer - height_nav;
    $('.main-container').css('min-height', height_container);
});
