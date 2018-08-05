from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, DestroyAPIView, RetrieveAPIView
from restaurants.models import Restaurant
from .serializers import RestaurantListSerializer
from .serializers import RestaurantDetailSerializer
from .serializers import RestaurantCreateSerializer

class RestaurantListView(ListAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantListSerializer

# Complete me
class RestaurantDetailView(RetrieveAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'restaurant_id'


# Complete me
class RestaurantUpdateView(RetrieveUpdateAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantCreateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'restaurant_id'




# Complete me
class RestaurantDeleteView(DestroyAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurantListSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'object_id'
