//メニューボタンクリック時の処理
document.addEventListener('DOMContentLoaded', function () {
  document.getElementById('menuButton').addEventListener('click', function () {
    this.classList.toggle('active');
    document.getElementById('MenuButtons').classList.toggle('active');
  })
});

//title image adjust
$(function () {
  var titleImage_width = $('#amaist-title-box').width();
  var adjust_width = titleImage_width * 0.6654;
  $('#amaist-title-box').height(adjust_width);
})