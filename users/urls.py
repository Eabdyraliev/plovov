from django.urls import path
from .views import (UserListCreateAPVIew, 
                    UserRetrieveUpdateAPIView)

urlpatterns = [
    path('', UserListCreateAPVIew.as_view(), name = 'user-list-create'),
    path('<int:pk>/', UserRetrieveUpdateAPIView.as_view(), name = 'user'),
]