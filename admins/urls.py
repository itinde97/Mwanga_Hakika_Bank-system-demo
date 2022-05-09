from django.urls import path
from .import views

app_name = "admins"

urlpatterns = [
    path("", views.index, name = "admin_index"),
]
