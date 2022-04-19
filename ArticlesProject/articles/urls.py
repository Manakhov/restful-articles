from django.urls import path
from .views import ArticleListCreateView, ArticleDetailView


urlpatterns = [
    path('article/', ArticleListCreateView.as_view()),
    path('article/<int:pk>/', ArticleDetailView.as_view())
]
