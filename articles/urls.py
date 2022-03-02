from django.urls import path

from .views import ArticleCreateView, ArticleDeletView, ArticleDetailView, ArticleListView, ArticleUpdateView



urlpatterns = [
    path('', ArticleListView.as_view(), name='articles'),
    path('article_detail/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('new_article/', ArticleCreateView.as_view(), name='new_article'),
    path('edit_article/<int:pk>', ArticleUpdateView.as_view(), name='edit_article'),
    path('delete_article/<int:pk>', ArticleDeletView.as_view(), name='delete_article'),
] 