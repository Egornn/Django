from django.urls import path
from .views import hello, HelloView
from .views import year_post, MonthPost, post_detail, my_view, TemplIf
from .views import detail_article, get_articles

urlpatterns = [
    path('hello/', hello, name='hello'),
    path('hello2/', HelloView.as_view(), name='hello2'),
    path('posts/<int:year>/', year_post, name='year_post'),
    path('posts/<int:year>/<int:month>/', MonthPost.as_view(), name='month_post'),
    path('posts/<int:year>/<int:month>/<slug:slug>/', post_detail, name='post_detail'),
    path('', my_view, name='index'),
    path('if/', TemplIf.as_view(), name='templ_if'),
    path('articles/<int:author_id>', get_articles, name='articles'),
    path('detail/<int:article_id>', detail_article, name='detail_article')
]
