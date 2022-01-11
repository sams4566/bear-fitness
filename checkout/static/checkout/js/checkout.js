$(function() {
    $(".checkout-list").slice(0, 4).show();
    $("#load-checkout-items").on('click', function() {
        $(".checkout-list:hidden").slice(0, 4).slideDown();
        if ($(".checkout-list:hidden").length == 0) {
            $("#load-checkout-items").hide();
        }
    });
});