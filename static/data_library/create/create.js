$('#tag-add-button').click(function () {
    $('#tag-box').append('<input type="text" multiple name="tags"/>')
})

$('#add-file-button').click(function () {
    $('#file-box').append('<input type="file" multiple name="data_file" class="data_file" id="id_data_file"></input>')
})