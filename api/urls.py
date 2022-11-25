from api import views
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', views.apiOverview,name='apiOverview'),
    path('taskList/', views.taskList,name='taskList'),
    path('taskDetail/<str:pk>/', views.taskDetail,name='taskDetail'),
    path('taskCreate/', views.taskCreate,name='taskCreate'),
    path('taskUpdate/<str:pk>/', views.taskUpdate,name='taskUpdate'),
    path('taskDelete/<str:pk>/', views.taskDelete,name='taskDelete'),
    path('taskPending/', views.taskPending,name='taskPending'),
    path('taskCompleted/', views.taskCompleted,name='taskCompleted'),








]
