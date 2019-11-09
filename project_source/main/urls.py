from django.contrib import admin
from django.urls import path, include
from .views import *
urlpatterns = [

    path('', HomePageView.as_view(), name="home"),
    path('dashboard', dashboard, name="dashboard"),
    path('dashboard-upload', DashboardUpload.as_view(), name="dashboard"),
    path('dashboard-soil', SoilHealthcare,name="soil"),
    path('dashboard-livestock', LivestockHealthcare,name="livestock"),
    path('upload', upload_leaf, name="upload_leaf"),
    path('upload-cassava', upload_cassava_leaf, name="upload_cassava_leaf"),
#    path('result/<int:pk>', result, name="result"),
    path('result/<int:pk>/<str:lang>', result, name="result"),
    path('edit/<int:pk>', edit, name="edit"),

]
