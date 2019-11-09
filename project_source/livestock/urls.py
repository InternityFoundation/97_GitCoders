from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [

    path('', category_a, name="category_a"),
    path('cat-b', category_b, name="category_b"),
    path('category-result', category_result, name="category_result"),

]
