from django.urls import path
from .views import ArticleViewSet


urlpatterns = [
    # path('', ArticleListCreateView.as_view()),
    # path('<int:pk>/', ArticleDetailView.as_view()),
    path('', ArticleViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('<int:pk>/', ArticleViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
]
