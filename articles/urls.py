from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/edit/',views.ArticleUpdateView.as_view(), name='article_edit'), # new
    path('<int:pk>/',views.ArticleDetailView.as_view(), name='article_detail'), # new
    path('<int:pk>/delete/',views.ArticleDeleteView.as_view(), name='article_delete'),
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('new/', views.ArticleCreateView.as_view(), name='article_new'),
    path('<int:pk>/comment/', views.CommentCreateView.as_view(), name='comment_new'),
]
