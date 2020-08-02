
from django.urls import path
from . import views

urlpatterns = [
    path('mentors', views.mentor_call, name='mentor-calls')
]
