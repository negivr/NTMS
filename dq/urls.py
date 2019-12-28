from django.urls import path
from . import views

app_name = 'dq'
urlpatterns = [
    path("", views.home, name="person-list"),
    path("detail/<int:pk>/", views.person_detail, name="person-detail"),
    path("person/create/", views.person_create, name="person-create"),
    path("person/update/<int:pk>", views.person_update, name="person-update"),
    path("cdls/", views.cdl_list, name="cdl-list"),
    path("cdl/create/", views.cdl_create, name="cdl-create"),
    path("cdl/create/<int:pk>/", views.person_cdl_create, name="person-cdl-create"),
]

