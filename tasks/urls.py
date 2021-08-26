from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.tasks, name='tasks'),
    path('delete/<pk>', views.TaskDeleteView.as_view(), name='Delete-task'),
    path('update/<pk>', views.TaskUpdateView.as_view(), name='Update-task'),
    path('add/', views.TaskCreatView.as_view(), name='Add-task')
    
]