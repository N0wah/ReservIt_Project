from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UsersListView.as_view(), name='user-list'),
    path('users/<int:id>/', views.UserRetrieveUpdateDestroy.as_view(), name='user-detail'),
    path('restaurants/', views.RestaurantListCreate.as_view(), name='restaurant-list'),
    path('restaurants/<int:id>/', views.RestaurantRetrieveUpdateDestroy.as_view(), name='restaurant-detail'),
    path('restaurants/owner_id/<int:owner_id>/', views.RestaurantByOwnerView.as_view(), name='restaurant-by-owner'),
    path('tables/', views.TableListCreate.as_view(), name='table-list'),
    path('tables/restaurant_id/<int:restaurant_id>/', views.TableByRestaurantView.as_view(), name='tables-by-restaurant'),
    path('reservations/', views.ReservationListCreate.as_view(), name='reservation-list'),
    path('reservations/<int:id>/', views.ReservationRetrieveUpdateDestroy.as_view(), name='reservation-detail'),
    path('reservations/user_id/<int:user_id>/', views.ReservationByUserView.as_view(), name='reservations-by-user'),
    path('favorites/', views.FavoriteListCreate.as_view(), name='favorite-list'),
    path('favorites/<int:id>/', views.FavoriteRetrieveUpdateDestroy.as_view(), name='favorite-detail'),
    path('login/', views.LoginView.as_view(), name='login'),
]
