$(function() {
    $(".checkout-list").slice(0, 2).show();
    $("#load-checkout-items").on('click', function() {
        $(".checkout-list:hidden").slice(0, 2).slideDown();
        if ($(".checkout-list:hidden").length == 0) {
            $("#load-checkout-items").hide();
        }
    });
});

$(function() {
    $(".order-list").slice(0, 4).show();
    $("#load-orders").on('click', function() {
        $(".order-list:hidden").slice(0, 4).slideDown();
        if ($(".order-list:hidden").length == 0) {
            $("#load-orders").hide();
        }
    });
});

$(function() {
    $(".order-summary-list").slice(0, 2).show();
    $("#load-order-summary-items").on('click', function() {
        $(".order-summary-list:hidden").slice(0, 2).slideDown();
        if ($(".order-summary-list:hidden").length == 0) {
            $("#load-order-summary-items").hide();
        }
    });
});

$(function() {
    $(".order-confirmation-list").slice(0, 2).show();
    $("#load-order-confirmation-items").on('click', function() {
        $(".order-confirmation-list:hidden").slice(0, 2).slideDown();
        if ($(".order-confirmation-list:hidden").length == 0) {
            $("#load-order-confirmation-items").hide();
        }
    });
});