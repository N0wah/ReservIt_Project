from rest_framework import serializers
from .models import Favorite, User, Restaurant, Table, Reservation
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    password_hash = serializers.CharField(write_only=False, required=True)
    avatar_path = serializers.CharField(required=False, allow_blank=True)

    def create(self, validated_data):
        if 'password_hash' in validated_data:
            validated_data['password_hash'] = make_password(validated_data['password_hash'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password_hash' in validated_data:
            validated_data['password_hash'] = make_password(validated_data['password_hash'])
        return super().update(instance, validated_data)

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password_hash': {'write_only': False}}

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ['id', 'user_id', 'restaurant_id']

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'owner_id', 'name', 'address', 'description', 'phone_number', 'email', 'images', 'opening_days']

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'restaurant_id', 'capacity', 'table_number', 'is_reserved']

class ReservationSerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), read_only=False)

    class Meta:
        model = Reservation
        fields = ['id', 'user_id', 'restaurant', 'table_id', 'reservation_time', 'reservation_date', "guest_count", 'status', 'information']