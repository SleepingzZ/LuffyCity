from rest_framework import serializers

from userinfo.models import UserInfo


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ['username', 'password']
