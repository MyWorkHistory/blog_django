from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogIndex),
    path('<str:catid>', views.blogIndexCat),
    path('details/<str:blogid>', views.articleDetails),
]