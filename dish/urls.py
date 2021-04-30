from django.urls import path
from .views import *

app_name = 'dish'

urlpatterns = [
    path('', DishListAPIView.as_view(), name = 'test'),
    # path('<int:pk>/', DishDetailAPIView.as_view(), name='dish'),
    path('create/', DishCreateAPIView.as_view(), name='create'),
    # path('<int:pk>/delete', DishDeleteAPIView.as_view(), name='delete'),
    path('<int:pk>/update', DishUpdateAPIView.as_view(), name='Update'),
    # path('<int:pk>/detail', DishDetailAPIView.as_view(), name='detail')
]