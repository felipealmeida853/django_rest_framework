from django.urls import path
from api_rest.views import api_overview, task_list, task_detail, task_create, task_update, task_delete

urlpatterns = [
    path('api/', api_overview),
    path('task-list/', task_list),
    path('task-detail/<str:pk>/', task_detail),
    path('task-create/', task_create),
    path('task-update/<str:pk>/', task_update),
    path('task-delete/<str:pk>/', task_delete),
]
