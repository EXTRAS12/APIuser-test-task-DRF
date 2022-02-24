from rest_framework import serializers

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    """Постраничное получение кратких данных обо всех пользователях, User"""
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'email', ]


class UserForAdminSerializer(serializers.ModelSerializer):
    """CRUD для админа"""
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'other_name', 'email', 'phone', 'birthday',
                  'city', 'additional_info', 'is_admin', 'password', ]


class UserCurrentSerializer(serializers.ModelSerializer):
    """Текущий юзер"""
    class Meta:
        model = CustomUser
        fields = ['id', 'first_name', 'last_name', 'other_name', 'email', 'phone', 'birthday',
                  'is_admin', ]


class UserUpdateSerializer(serializers.ModelSerializer):
    """Изменение данных пользователя"""
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'other_name', 'email', 'phone', 'birthday', ]

