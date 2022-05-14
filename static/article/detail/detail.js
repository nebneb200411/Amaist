$(function() {
    var navSelector = "#toc-nav";
    var $myNav = $(navSelector);

    $("#article-content-box").scrollspy({
        $nav: $("#toc-nav"),
        $scope: $("#article-content-box"),
        offset: 10,
    });
});