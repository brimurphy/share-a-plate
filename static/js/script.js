$(document).ready(function () {
    $('.sidenav').sidenav({ edge: "right" });
    $('select').formSelect();
    // previous page
    $(".btn-back").click(function () {
        window.history.back();
    });
});
