
from django.urls import path
from .views import boards_view, single_board_view

urlpatterns = [
    path('', boards_view, name='boards_view'),
    path('<int:board_id>/', single_board_view, name='single_board_view'),
]