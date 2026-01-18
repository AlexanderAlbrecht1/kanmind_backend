
from django.urls import path
from .views import tasks_view, single_task_view

urlpatterns = [
    path('', tasks_view, name='tasks_view'),
    path('<int:task_id>/', single_task_view, name='single_task_view')
]