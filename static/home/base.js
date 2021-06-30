window.addEventListener('DOMContentLoaded', function () {
    $(document).ready(function () {
        hsize = $(window).height();
        $("html").css("height", hsize + "px");
    }

    );

    $(window).resize(function () {
        hsize = $(window).height();
        $("html").css("height", hsize + "px");
    }

    );
}

);

window.addEventListener('DOMContentLoaded', function () {
    $(document).ready(function () {
        hsize = $(window).height();
        $("body").css("height", hsize + "px");
    }

    );

    $(window).resize(function () {
        hsize = $(window).height();
        $("body").css("height", hsize + "px");
    }

    );
}

);

//ナビゲーションより下に対してはナビゲーションの高さを考慮した位置に配置
//ナビゲーションの高さ取得
//let navigation_bar_height = document.getElementById("header-nav-box").clientHeight;
//位置および高さの変更
//var element = document.getElementById("under-header");
//element.style.height = hsize - navigation_bar_height + "px";
//element.style.top = navigation_bar_height + "px";

//メニューボタンクリック時の処理
$('.menu-button').on('click', function () {
    $('.menu-button').toggleClass('clicked');
    $('.header-nav').toggleClass('slide-in');
}

);

//プルアップメニューの表示
$('#article-icon').on('click', function () {
    $('.hide-and-appear-article').toggleClass('appear');
}
);

$('#datalibrary-icon').on('click', function () {
    $('.hide-and-appear-datalibrary').toggleClass('appear');
}
);

$('#profile-icon').on('click', function () {
    $('.hide-and-appear-profile').toggleClass('appear');
}
);

$('#question-icon').on('click', function () {
    $('.hide-and-appear-question').toggleClass('appear');
}
);

$('#createarticle-icon').on('click', function () {
    $('.hide-and-appear-createarticle').toggleClass('appear');
}
);

$('#hide-and-appear').click(function () {
    $('.footer-menu').toggleClass('crash');
    $('.appearing-menu').toggleClass('deep');
    $('.menu-class').toggleClass('hidden');
    $('.hide-and-appear-class').toggleClass('up');
});