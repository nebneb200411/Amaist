var canvas = document.getElementById('menuButton');
if (canvas.getContext){
  var ctx = canvas.getContext('2d');
  //パスをリセット
  ctx.beginPath();
  //円の中心座標:(0,0)ただし、1/4の円
  //半径:200
  //開始角度0rad
  //時計回りで書く
  ctx.arc(0, 0, 60, 0, 90*Math.PI, false);
  ctx.stroke();
  ctx.fillStyle = '#066391';
  ctx.fill();
  ctx.closePath();
  //pathをリセットして内のデザインを描画
  ctx.beginPath();
  ctx.arc(0, 0, 50, 0, 90*Math.PI, false);
  ctx.stroke();
  ctx.fillStyle = '#077766';
  ctx.fill();
  ctx.closePath();
}

//メニューボタンクリック時の処理
document.addEventListener('DOMContentLoaded', function(){
  document.getElementById('menuButton').addEventListener('click', function() {
    this.classList.toggle('active');
    document.getElementById('MenuButtons').classList.toggle('active');
  })
});