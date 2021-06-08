from django.urls import path
from .views import *

urlpatterns = [
    # path("", index, name="home"),
    path("", HomeViews.as_view(), name="home"),
    # path("category/<int:category_id>/", get_category, name="category"),
    path("category/<int:category_id>/", NewsByCategory.as_view(), name="category"),
    path("news/<int:pk>/", ViewNews.as_view(), name="views_news"),
    # path("news/<int:news_id>/", views_news, name="views_news"),
    path("news/add-news/", CreateNews.as_view(), name="add_news"),
    # path("news/add-news/", add_news, name="add_news"),
]
