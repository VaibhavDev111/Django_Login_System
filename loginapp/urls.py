from django.contrib import admin
from django.urls import path
from loginapp.views import (retrieveUserData, enterExitUser)

urlpatterns = [
    path('user_info/<int:id>', retrieveUserData.as_view(), name="user_info"),
    path('enter_exit/<int:uid>', enterExitUser.as_view(), name="enter_exit"),
]
