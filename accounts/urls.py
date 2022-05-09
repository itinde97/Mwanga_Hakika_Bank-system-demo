from . import views
from django.urls import path
app_name = "accounts"

urlpatterns = [
    path("register/", views.register, name = "signup"),
    path("login/", views.sign_in, name = "signin"),
    path("logout/", views.logout_view, name = "logout"),
]
