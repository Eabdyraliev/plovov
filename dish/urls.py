from django.urls import path
from .views import PlovosAPIView

app_name = 'dish'

urlpatterns = [
    path('', DishListAPIView.as_view(), name = 'test')
]