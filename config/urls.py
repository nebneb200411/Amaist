"""WebApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from registration import views
from . import settings
from django.conf.urls.static import static

# admin.site.site_title = 'WebApp管理サイト'
# admin.site.site_header = 'WebApp管理サイト'
# admin.site.index_title = 'メニュー'
# admin.site.disable_action('delete_selected')

index_view = TemplateView.as_view(template_name='artcile/index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('registration/', views.SignUpView.as_view(), name='sign_up'),
    path('summernote/', include('django_summernote.urls')),
    path('', include('article.urls')),
    path('profile/', include('registration.urls')),
    path('profiles/', include('profiles.urls')),
    path('data_library/', include('data_library.urls')),
    path('question/', include('question.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

# 開発環境なので以下を設定
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
