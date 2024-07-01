# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from mnemonic import Mnemonic
from bitcoinlib.keys import HDKey
from bitcoinlib.networks import Network
from .serializers import DogecoinAddressGeneratorSerializer

@api_view(['POST'])
def doge_address_generator(request):
    serializer = DogecoinAddressGeneratorSerializer(data=request.data)
    if serializer.is_valid():
        try:
            user_id = serializer.validated_data['userId']

            # Create a new mnemonic phrase
            mnemo = Mnemonic("english")
            phrase = mnemo.generate()

            # Derive the seed from the mnemonic phrase
            seed = mnemo.to_seed(phrase)

            # Configure the Dogecoin network
            doge_network = Network('dogecoin')
            key = HDKey.from_seed(seed, network=doge_network)

            # Derive the Dogecoin address
            dogecoin_address = key.address()

            # Return the generated address as a JSON response
            return Response({'dogeAddress': dogecoin_address}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
