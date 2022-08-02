from django.urls import path
from . import views

app_name = 'registration'

urlpatterns = [
    path('', views.SignUpView.as_view(), name = 'sign_up'),
    #path('delete_confirm/', views.UserDeleteConfirmView.as_view(), name='delete_confirm'),
    #path('delete/<uuid:pk>', views.UserDeleteView.as_view(), name="delete"),
]
