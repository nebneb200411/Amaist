$('#addon-wrapping').click(function () {
    $('#tag').append('<input type="text" name="tags" class="form-control" aria-label="Sizing example input" aria-describedby="inputGroup-sizing-default" multiple>')
})

$(function () {
    var page_title_image = $('#page-title-box');
    page_title_image.height(page_title_image.width() * 0.4);

    $('#check-box').on('click', function () {
        $('#check-icon').toggleClass('visible');
    });
})

$('#publish-or-not').change(function() {
    
    $('#publish-or-not:checked').each(function() {
        var r = $(this).prop('checked');
        
        console.log(r);
    })
    
})

$('#genre-error-delete-button').click(function() {
    $('#genre-error').remove()
})

$('#title-error-delete-button').click(function() {
    $('#title-error').remove()
})

$('#content-error-delete-button').click(function() {
    $('#content-error').remove()
})