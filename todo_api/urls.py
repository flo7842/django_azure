
from django.urls import re_path, include
from .views import (
    TodoListApiView,
)

urlpatterns = [
    re_path('api', TodoListApiView.as_view()),
]