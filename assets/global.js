$(function () {
    $('[data-toggle="tooltip"]').tooltip()
  })

  $(window).ready(function(){
    // const is_navside_open = $.cookie("is_navside_open");
    $('form').not('.modalform').submit(function(){
        $("button[type=submit]",this).html('<i class="fa fa-refresh fa-spin"></i> ');
        window.setTimeout(function() {
            $(".loader").fadeIn("slow");
        }, 500);

    });
    if (sessionStorage.scrollTop != "undefined") {
        $('#mySidenav').scrollTop(sessionStorage.scrollTop);
    }
});