from rest_framework import serializers

from .models import Dish


class DishListSerialize(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = ('id', 'name', 'price')