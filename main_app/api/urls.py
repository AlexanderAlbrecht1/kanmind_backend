
from django.urls import path
from .views import boards_view

urlpatterns = [
    path('', boards_view, name='boards_view'),
    path('<int:board_id>/', boards_view, name='boards_view'),
]