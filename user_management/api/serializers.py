from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ("id", "username", "email", "first_name", "last_name", "bio")
        model = User
