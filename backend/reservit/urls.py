"""
URL configuration for reservit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.UsersListView.as_view(), name='user-list'),
    path('users/<int:id>/', views.UserRetrieveUpdateDestroy.as_view(), name='user-detail'),
    path('restaurants/', views.RestaurantListCreate.as_view(), name='restaurant-list'),
    path('restaurants/<int:id>/', views.RestaurantRetrieveUpdateDestroy.as_view(), name='restaurant-detail'),
    path('tables/', views.TableListCreate.as_view(), name='table-list'),
    path('reservations/', views.ReservationListCreate.as_view(), name='reservation-list'),
    path('favorites/', views.FavoriteListCreate.as_view(), name='favorite-list'),
    path('favorites/<int:id>/', views.FavoriteRetrieveUpdateDestroy.as_view(), name='favorite-detail'),
    path('login/', views.LoginView.as_view(), name='login'),
]
