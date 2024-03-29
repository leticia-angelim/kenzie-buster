from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(
        max_length=20,
        validators=[
            UniqueValidator(queryset=User.objects.all(), message="username already taken."),
        ],
    )
    email = serializers.EmailField(
        max_length=127,
        validators=[
            UniqueValidator(queryset=User.objects.all(), message="email already registered."),
        ],
    )
    birthdate = serializers.DateField(required=False)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    password = serializers.CharField(write_only=True)
    is_employee = serializers.BooleanField(default=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data: dict) -> User:
        if validated_data["is_employee"]:
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)
