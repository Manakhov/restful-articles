from django.urls import path
from .views import ArticleCreateView, ArticlesListView


urlpatterns = [
    path('article/create/', ArticleCreateView.as_view()),
    path('article/', ArticlesListView.as_view()),
]
