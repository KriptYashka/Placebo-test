from django.contrib import admin
from django.urls import path

from app import views
from app import api

urlpatterns = [
    path('', views.index_page, name="index"),
    path('api/departament/', api.DepartamentList.as_view()),
    path('api/departament/<int:pk>', api.DepartamentDetail.as_view())
]
