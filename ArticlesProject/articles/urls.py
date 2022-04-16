from django.urls import path
from .views import ArticleCreateView, ArticlesListView, ArticleDetailView


urlpatterns = [
    path('article/create/', ArticleCreateView.as_view()),
    path('article/', ArticlesListView.as_view()),
    path('article/<int:pk>/', ArticleDetailView.as_view())
]
