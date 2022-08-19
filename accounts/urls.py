from django.urls import path

from . import views as account_views

urlpatterns = [
    path('signup/', account_views.SignUp.as_view(), name='signup'),
    ]
