from django.urls import path
from . import views

app_name = 'data_library'
urlpatterns = [
    path('create/', views.DataLibraryCreateView.as_view(), name='create'),
    path('update/<uuid:pk>/', views.DataLibraryUpdateView.as_view(), name='update'),
    path('', views.DataLibraryListView.as_view(), name='list'),
    path('detail/<uuid:pk>/', views.DataLibraryDetailView.as_view(), name='detail'),
    path('good_count/', views.good_count, name='good_count'),
    path('comment/', views.comment, name='comment'),
]
