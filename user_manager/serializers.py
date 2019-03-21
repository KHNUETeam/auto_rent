from rest_framework import serializers
from user_manager.models import MyUser


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer of user
    """

    class Meta:
        model = MyUser
        fields = ('id', 'email', 'first_name', 'last_name', 'patronymic', 'date_of_birth', 'is_admin', 'is_verified')

