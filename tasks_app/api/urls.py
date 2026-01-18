
from django.urls import path
from .views import tasks_view

urlpatterns = [
    path('', tasks_view, name='tasks_view'),
  #  path('<int:board_id>/', single_board_view, name='single_board_view'),
]