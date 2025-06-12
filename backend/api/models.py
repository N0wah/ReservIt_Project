# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=100)
    family_name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    password_hash = models.CharField(max_length=300)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} {self.family_name} ({self.email})"

    def check_password(self, raw_password):
        from django.contrib.auth.hashers import check_password
        return check_password(raw_password, self.password_hash)

class Favorite(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    restaurant_id = models.ForeignKey('Restaurant', on_delete=models.CASCADE, related_name='favorited_by')

    class Meta:
        unique_together = ('user_id', 'restaurant_id')

    def __str__(self):
        return f"{self.user.name} ❤️ {self.restaurant.name}"



class Restaurant(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    email = models.EmailField(max_length=150, blank=True, null=True)
    phone_number = models.CharField(max_length=150, blank=True, null=True)
    images = models.CharField(max_length=255, blank=True, null=True)
    opening_days = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
    
class Reservation(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    table_id = models.ForeignKey('Table', on_delete=models.CASCADE)
    guest_count = models.IntegerField(default=1)
    reservation_time = models.TimeField(blank=True, null=True)
    reservation_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True)
    information = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.name} @ {self.restaurant.name} on {self.date}"

class Table(models.Model):
    restaurant_id = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    table_number = models.IntegerField()
    capacity = models.IntegerField()
    is_reserved = models.BooleanField(default=False)

    def __str__(self):
        return f"Table {self.id} ({self.capacity}p) - {self.restaurant_id.name}"

