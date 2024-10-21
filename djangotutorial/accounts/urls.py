from django.urls import include, path

from . import views

urlpatterns = [
    path("sign-up", views.sign_up, name="sign_up"),
    path("log-out", views.logout, name="logout")
]
