from django.urls import path
from .views import ArticleCreateView


urlpatterns = [
    path('article/create/', ArticleCreateView.as_view())
]
