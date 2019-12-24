from django.urls import path
from . import views

app_name = 'dq'
urlpatterns = [
    path("", views.home, name="people"),
    path("detail/<int:pk>/", views.person_detail, name="person-detail"),
]

