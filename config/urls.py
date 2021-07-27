from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from registration import views
from . import settings
from django.conf.urls.static import static
from django.views.decorators.cache import never_cache
from ckeditor_uploader import views as ckeditor_views

index_view = TemplateView.as_view(template_name='artcile/index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('registration/', views.SignUpView.as_view(), name='sign_up'),
    path('/activate/<uidb64>/<token>/',
         views.ActivateView.as_view(), name="activate"),
    path('', include('article.urls')),
    path('profile/', include('registration.urls')),
    path('profiles/', include('profiles.urls')),
    path('data_library/', include('data_library.urls')),
    path('question/', include('question.urls')),
    path('ckeditor/upload/', login_required(ckeditor_views.upload),
         name='ckeditor_upload'),
    path('ckeditor/browse/', never_cache(login_required(ckeditor_views.browse)),
         name='ckeditor_browse'),
    path('notifications/', include('notifications.urls')),
]

# 開発環境なので以下を設定
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
