$(function () {
    $('.service-term').on('change', function () {
        if ($(this).is(':checked')) {
            $('#register-button').prop('disabled', false);
        }
        else {
            $('#register-button').prop('disabled', true);
        }
    });
});