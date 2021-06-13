from django.urls import path
from . import views

app_name = 'question'

urlpatterns = [
    path('', views.QuestionListView.as_view(), name="list"),
    path('create/', views.QuestionCreateView.as_view(), name="create"),
    path('detail/<int:pk>', views.QuestionDetailView.as_view(), name="detail"),
    path('good_count/', views.good_count, name="good_count"),
    path('comment/', views.comment, name="comment"),
]
