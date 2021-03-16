window.addEventListener('DOMContentLoaded', function(){
    $(document).ready(function () {
        hsize = $(window).height();
        $("html").css("height", hsize + "px");
    });
    $(window).resize(function () {
        hsize = $(window).height();
        $("html").css("height", hsize + "px");
    });
});

window.addEventListener('DOMContentLoaded', function(){
    $(document).ready(function () {
        hsize = $(window).height();
        $("body").css("height", hsize + "px");
    });
    $(window).resize(function () {
        hsize = $(window).height();
        $("body").css("height", hsize + "px");
    });
});

//ナビゲーションより下に対してはナビゲーションの高さを考慮した位置に配置
//ナビゲーションの高さ取得
//let navigation_bar_height = document.getElementById("header-nav-box").clientHeight;
//位置および高さの変更
//var element = document.getElementById("under-header");
//element.style.height = hsize - navigation_bar_height + "px";
//element.style.top = navigation_bar_height + "px";


var canvas = document.getElementById('menu-button-id');
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
    document.getElementById('menu-button-id').addEventListener('click', function() {
        this.classList.toggle('active');
        document.getElementById('MenuButtons').classList.toggle('active');
    })
});

//under-header要素について，画面サイズ-ヘッダーの高さによって，画面際にぴったり合うようにする．
//また，header-navの高さはヘッダーの高さに合わせる
//header_heightの高さ取得および，windowサイズの取得
var header_height = document.getElementsByClassName('header-nav-box').clientHeight;
var window_height = window.innerHeight;
//heade-navのheight, topにアクセスし，それぞれの値を指定
var under_header = document.getElementById('under-header-id');
window.onload = function() {
    under_header_height = window_height - header_height;
    under_header.style.height = under_header_height + 'px';
    under_header.style.top = header_height + 'px';
}