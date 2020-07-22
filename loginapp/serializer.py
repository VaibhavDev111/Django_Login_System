from rest_framework import serializers
from loginapp.models import (UserInfo, EnterExitInfo)


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'


class EnterExitSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnterExitInfo
        fields = '__all__'

