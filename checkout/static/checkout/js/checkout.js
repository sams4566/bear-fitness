/*jshint esversion: 6 */

/**
 * Reveals and hides the 'More Items' button when there
 * are more items available to view in checkout.html
*/ 
$(function() {
    $(".checkout-list").slice(0, 2).show();
    $("#load-checkout-items").on('click', function() {
        $(".checkout-list:hidden").slice(0, 2).slideDown();
        if ($(".checkout-list:hidden").length == 0) {
            $("#load-checkout-items").hide();
        }
    });
});

/**
 * Reveals and hides the 'More Orders' button when there
 * are more orders available to view in the orders.html
*/ 
$(function() {
    $(".order-list").slice(0, 4).show();
    $("#load-orders").on('click', function() {
        $(".order-list:hidden").slice(0, 4).slideDown();
        if ($(".order-list:hidden").length == 0) {
            $("#load-orders").hide();
        }
    });
});

/**
 * Reveals and hides the 'More Items' button when there
 * are more items available to view in 
 * order_summary.html
*/ 
$(function() {
    $(".order-summary-list").slice(0, 2).show();
    $("#load-order-summary-items").on('click', function() {
        $(".order-summary-list:hidden").slice(0, 2).slideDown();
        if ($(".order-summary-list:hidden").length == 0) {
            $("#load-order-summary-items").hide();
        }
    });
});

/**
 * Reveals and hides the 'More Items' button when there
 * are more items available to view in 
 * checkout_confirmation.html
*/ 
$(function() {
    $(".order-confirmation-list").slice(0, 2).show();
    $("#load-order-confirmation-items").on('click', function() {
        $(".order-confirmation-list:hidden").slice(0, 2).slideDown();
        if ($(".order-confirmation-list:hidden").length == 0) {
            $("#load-order-confirmation-items").hide();
        }
    });
});