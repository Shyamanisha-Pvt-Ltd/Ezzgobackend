from django.contrib import admin
from django.urls import path, include
from .views import getPhoneNumberRegisteredView

urlpatterns = [
    path("<phone>/", getPhoneNumberRegisteredView.as_view(), name="OTP Gen"),
    # path('register', getPhoneNumberRegisteredView.as_view()),
    # path('login', LoginView.as_view()),
    # path('user', UserView.as_view()),
    # path('logout', LogoutView.as_view())
]
