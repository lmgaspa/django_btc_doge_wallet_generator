from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from mnemonic import Mnemonic
from bitcoinlib.keys import HDKey
from .serializers import BitcoinAddressGeneratorSerializer

@api_view(['POST'])
def btc_address_generator(request):
    serializer = BitcoinAddressGeneratorSerializer(data=request.data)
    if serializer.is_valid():
        try:
            user_id = serializer.validated_data['userId']

            # Create a new mnemonic phrase
            mnemo = Mnemonic("english")
            phrase = mnemo.generate()

            # Derive the seed from the mnemonic phrase
            seed = mnemo.to_seed(phrase)

            # Derive the private key and address directly from the seed
            key = HDKey.from_seed(seed)
            public_key = key.wif()
            address = key.address()

            # Return the generated address as a JSON response
            return Response({'btcaddress': address}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
