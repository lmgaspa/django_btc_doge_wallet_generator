from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from mnemonic import Mnemonic
from solana.keypair import Keypair
from .serializers import SolanaAddressGeneratorSerializer

@api_view(['POST'])
def solanaaddressgenerator(request):
    serializer = SolanaAddressGeneratorSerializer(data=request.data)
    if serializer.is_valid():
        try:
            user_id = serializer.validated_data['userId']

            # Create a new mnemonic phrase
            mnemo = Mnemonic("english")
            phrase = mnemo.generate()

            # Derive the seed from the mnemonic phrase
            seed = mnemo.to_seed(phrase)

            # Generate a Solana keypair from the seed
            keypair = Keypair.from_seed(seed[:32])  # Solana seed must be 32 bytes
            public_key = keypair.public_key
            address = public_key.to_base58().decode('utf-8')

            # Return the generated address as a JSON response
            return Response({'solana_address': address}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
