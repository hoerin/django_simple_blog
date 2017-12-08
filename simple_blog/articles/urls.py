from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name = 'articles'

urlpatterns = [
    path('list/', ArticleListView.as_view(), name='list'),
    path('detail/<int:pk>/', ArticleDetailView.as_view(), name='detail'),
    path('create/', ArticleCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ArticleUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete'),
]
