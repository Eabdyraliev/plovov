from rest_frameworks.views import APIView
from rest_framework.response import Response

# Create your views here.
class PlovoAPIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response({'test': 'test'})