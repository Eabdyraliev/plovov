from rest_frameworks.views import APIView
from rest_framework.response import Response
from .models import Dish
from .serializers import DishListSerialize


# Create your views here.
class PlovoAPIView(APIView):
    def get(self, request, *args, **kwargs):
        dishes = Dish.object.order_by('name')
        dishes_serialized = DishListSerializer(dishes, many = True)
       return Response(data = dishes_serialized.data)
