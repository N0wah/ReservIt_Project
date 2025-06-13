from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Reservation
from .serializers import ReservationSerializer

from .models import User, Restaurant, Table, Favorite, Reservation
from .serializers import RestaurantSerializer, TableSerializer, ReservationSerializer, FavoriteSerializer, UserSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.conf import settings
import os
from django.utils.text import slugify

class RestaurantByOwnerView(APIView):
    def get(self, request, owner_id):
        restaurants = Restaurant.objects.filter(owner_id=owner_id)
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

class UsersListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'


class RestaurantListCreate(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class RestaurantRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    lookup_field = 'id'

class TableListCreate(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class TableByRestaurantView(APIView):
    def get(self, request, restaurant_id):
        tables = Table.objects.filter(restaurant_id=restaurant_id)
        serializer = TableSerializer(tables, many=True)
        return Response(serializer.data)

class ReservationListCreate(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

class ReservationRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    lookup_field = 'id'


class FavoriteListCreate(generics.ListCreateAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

class FavoriteRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    lookup_field = 'id'

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                serializer = UserSerializer(user)
                return Response({'token': 'dummy-token', 'user': serializer.data})
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        except User.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class ReservationByUserView(APIView):
    def get(self, request, user_id):
        reservations = Reservation.objects.filter(user_id=user_id)
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data)

class RestaurantImageUploadView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, restaurant_id):
        try:
            restaurant = Restaurant.objects.get(id=restaurant_id)
        except Restaurant.DoesNotExist:
            return Response({'error': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)

        files = request.FILES.getlist('images')
        if not files:
            return Response({'error': 'No images uploaded'}, status=status.HTTP_400_BAD_REQUEST)

        # Directory: /frontend/reservit/public/img/restaurants/<restaurant_name_slug>/
        restaurant_name_slug = slugify(restaurant.name)
        base_dir = os.path.join(settings.BASE_DIR, 'frontend', 'reservit', 'public', 'img', 'restaurants', restaurant_name_slug)
        os.makedirs(base_dir, exist_ok=True)

        image_paths = []
        for file in files:
            filename = file.name
            file_path = os.path.join(base_dir, filename)
            # Avoid overwriting: add suffix if file exists
            base, ext = os.path.splitext(filename)
            counter = 1
            while os.path.exists(file_path):
                filename = f"{base}_{counter}{ext}"
                file_path = os.path.join(base_dir, filename)
                counter += 1
            with open(file_path, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            # Store relative path for frontend
            rel_path = f"/img/restaurants/{restaurant_name_slug}/{filename}"
            image_paths.append(rel_path)

        # Update images field (comma-separated)
        restaurant.images = ','.join(image_paths)
        restaurant.save()
        return Response({'images': image_paths}, status=status.HTTP_200_OK)
