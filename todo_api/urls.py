
from django.urls import path, include
from .views import (
    TodoListApiView,
)

urlpatterns = [
    path('todos', TodoListApiView.as_view()),
]