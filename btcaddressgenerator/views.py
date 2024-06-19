from rest_framework.decorators import api_view
from rest_framework.response import Response
from mnemonic import Mnemonic
from bitcoinlib.keys import HDKey

@api_view(['POST'])
def btcaddressgenerator(request):
    user_id = request.data.get('userId')
    if not user_id:
        return Response({'error': 'User ID is required'}, status=400)

    # Create a new mnemonic phrase
    mnemo = Mnemonic("english")
    phrase = mnemo.generate()

    # Derive the seed from the mnemonic phrase
    seed = mnemo.to_seed(phrase)

    # Derive the private key and address directly from the seed
    key = HDKey.from_seed(seed)
    address = key.address()

    # Return the generated address as a JSON response
    return Response({'btcaddress': address})