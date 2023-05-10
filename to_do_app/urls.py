from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='tasks_list'),
    path('update/<str:pk>/', views.updateTask, name='task_update'),
    path('delete/<str:pk>/', views.deleteTask, name='task_delete'),
]
