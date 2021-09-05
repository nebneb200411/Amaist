$('#tag-add-button').click(function () {
    $('#tag-box').append('<input type="text" multiple name="tags" class="tag-input" placeholder="&#xf02b;tag"/>')
})

$(function () {
    var page_title_image = $('#page-title-box');
    page_title_image.height(page_title_image.width() * 0.4);
})