from django.urls import path

from app import api, views

urlpatterns = [
    path('', views.index_page, name="index"),

    path('api/departament/', api.DepartamentList.as_view()),
    path('api/departament/<int:pk>', api.DepartamentDetail.as_view()),

    path('api/position/', api.PositionList.as_view()),
    path('api/position/<int:pk>', api.PositionDetail.as_view()),

    path('api/permission/', api.PermissionList.as_view()),
    path('api/permission/<int:pk>', api.PermissionDetail.as_view()),

    path('api/employee/', api.EmployeeList.as_view()),
    path('api/employee/<int:pk>', api.EmployeeDetail.as_view()),
]
