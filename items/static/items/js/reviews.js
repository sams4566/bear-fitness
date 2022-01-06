$(function() {
    $(".review-list").slice(0, 4).show();
    $("#load-reviews").on('click', function() {
        $(".review-list:hidden").slice(0, 4).slideDown();
        if ($(".review-list:hidden").length == 0) {
            $("#load-reviews").hide();
        }
    });
});