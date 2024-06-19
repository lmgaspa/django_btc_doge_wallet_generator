# myapp/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema

from .serializers import ExampleSerializer

class ExampleAPIView(APIView):
    @swagger_auto_schema(
        request_body=ExampleSerializer,
        responses={200: ExampleSerializer}
    )
    def post(self, request, *args, **kwargs):
        """
        Exemplo de endpoint POST.
        """
        serializer = ExampleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = serializer.validated_data['text']
        return Response({'text': text})
