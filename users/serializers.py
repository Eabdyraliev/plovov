from django.contrib.auth.models import get_user_model
from django_restframework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')