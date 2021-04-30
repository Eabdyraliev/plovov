from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import *
from .models import Order

class OrderListCreateView(APIView):
    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.POST)
        if serializer.is_valid():
            order_object = serializer.save()
            json_serializer = OrderSerializer(instance=order_object)
            return Response(data=json_serializer.data, status=201)
        return Response(data=serializer.errors)


class OrderView(APIView):
    def get(self, request, *args, **kwargs):
        order= Order.objects.get(pk=kwargs.get('pk'))
        serializer = OrderSerializer(instance=order)
        return Response(data=serializer.data)

    def put(self, request, *args, **kwargs):
        order= Order.objects.get(pk=kwargs.get('pk'))
        serializer = OrderSerializer(instance=order, data=request.data)
        if serializer.is_valid():
            serializer.save()

    def delete(self, request, *args, **kwargs):
        order= Order.objects.get(pk=kwargs.get('pk'))
        order.delete
        return Response(data={'message': 'Order successfull deleted'})