//navigation
$(function(){
    $('#navigation li').hover(function(){
        $(this).toggleClass('selected');
        $("ul:not(:animated)", this).slideDown();
    }, function(){
        $(this).removeClass('selected');
        $("ul.sub-nav",this).slideUp();
    });
});

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

//メニューボタンクリック時の処理
$('.menu-button').on('click', function () {
    $('.header-nav').toggleClass('slide-in');
    $('.top-line').toggleClass('clicked-top');
    $('.middle-line').toggleClass('clicked-middle');
    $('.bottom-line').toggleClass('clicked-bottom');
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

// adjust footer-icon
$(function () {
    var footer_icon = $('#footer-icon');
    var app_title = $('.app-title');
    footer_icon.height(app_title.height());
    footer_icon.width(footer_icon.height());
})