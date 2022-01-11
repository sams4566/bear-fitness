$(function() {
    $(".basket-list").slice(0, 4).show();
    $("#load-basket-items").on('click', function() {
        $(".basket-list:hidden").slice(0, 4).slideDown();
        if ($(".basket-list:hidden").length == 0) {
            $("#load-basket-items").hide();
        }
    });
});