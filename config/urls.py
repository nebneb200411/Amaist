from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from registration import views
from . import settings
from django.conf.urls.static import static
from django.views.decorators.cache import never_cache
from ckeditor_uploader import views as ckeditor_views
from django.contrib.sitemaps.views import sitemap

"""
around site map
"""
from .sitemaps import ArticleSiteMaps

sitemaps = {
     'article': ArticleSiteMaps,
}


urlpatterns = [
    path('', include('index.urls')),
    path('registration/<username>/',
         views.SignUpConfirmationView.as_view(), name="sign_up_confirm"),
    path('AmaistStaffAdminSite/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('registration/', views.SignUpView.as_view(), name='sign_up'),
    path('password_reset/', views.MyPasswordResetView.as_view(),
         name='password_reset'),
    path('activate/<uidb64>/<token>/',
          views.ActivateView.as_view(), name='activate'),
    path('article/', include('article.urls')),
    path('profile/', include('registration.urls')),
    path('profiles/', include('profiles.urls')),
    path('data_library/', include('data_library.urls')),
    path('question/', include('question.urls')),
    path('ckeditor/upload/', login_required(ckeditor_views.upload),
         name='ckeditor_upload'),
    path('ckeditor/browse/', never_cache(login_required(ckeditor_views.browse)),
         name='ckeditor_browse'),
    path('notifications/', include('notifications.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name="sitemaps"),
]

# 開発環境なので以下を設定
if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
