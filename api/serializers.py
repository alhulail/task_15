from rest_framework import serializers
from restaurants.models import Restaurant

class RestaurantListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
        	'name',
            'id',
        	'opening_time',
        	'closing_time',
        	]

class RestaurantDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
        	'name',
        	'opening_time',
        	'closing_time',
        	]

class RestaurantCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = [
        	'name',
        	'opening_time',
        	'closing_time',
        	]
