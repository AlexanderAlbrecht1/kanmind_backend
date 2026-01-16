
from django.urls import path
from .views import single_board_view

urlpatterns = [
    path('', single_board_view, name='single_board'),
]