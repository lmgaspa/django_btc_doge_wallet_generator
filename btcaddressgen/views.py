# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from .serializers import BitcoinAddressGeneratorSerializer
import bitcoinlib

class BitcoinAddressAPIView(APIView):
    @swagger_auto_schema(
        responses={200: BitcoinAddressGeneratorSerializer}
    )
    def post(self, request, *args, **kwargs):
        """
        Endpoint que gera um endereço de carteira Bitcoin.
        """
        # Gera um novo endereço de carteira Bitcoin
        bitcoin_address = bitcoinlib.keys.BitcoinKey().address

        # Retorna o endereço gerado como resposta
        return Response({'bitcoin_address': bitcoin_address})
