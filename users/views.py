from rest_framework.generics, import ListCreateAPIView, 
                                     RetriveUpdateDestroyAPIView

from .serializers import UserSerializer

from django.contrib.auth import get_user_model
from django_restframework import serializers

User = get_user_model()

class UserListCreateAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()



class UserRetriveUpdateDestroyAPVIew(RetriveUpdateDestroy):
    serializer_class = UserSerializer
    queryset = User.objects.all()
