from bitcoinlib.networks import Network
from django.http import JsonResponse
from mnemonic import Mnemonic
from bitcoinlib.keys import HDKey
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(
    method='get',
    operation_description="Create a new Bitcoin wallet",
    responses={200: openapi.Response('Wallet data', openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'mnemonic': openapi.Schema(type=openapi.TYPE_STRING, description='Mnemonic phrase'),
            'seed': openapi.Schema(type=openapi.TYPE_STRING, description='Seed in hex format'),
            'private_key': openapi.Schema(type=openapi.TYPE_STRING, description='WIF private key'),
            'bitcoin_address': openapi.Schema(type=openapi.TYPE_STRING, description='Bitcoin address')
        }
    ))}
)
@api_view(['GET'])
def create_wallets_btc(request):
    mnemo = Mnemonic("english")
    phrase = mnemo.generate()
    seed = mnemo.to_seed(phrase)
    key = HDKey.from_seed(seed)
    private_key = key.wif()
    bitcoin_address = key.address()

    data = {
        'mnemonic': phrase,
        'seed': seed.hex(),
        'private_key': private_key,
        'bitcoin_address': bitcoin_address
    }

    return JsonResponse(data)

@swagger_auto_schema(
    method='get',
    operation_description="Create a new Dogecoin wallet",
    responses={200: openapi.Response('Wallet data', openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'mnemonic': openapi.Schema(type=openapi.TYPE_STRING, description='Mnemonic phrase'),
            'seed': openapi.Schema(type=openapi.TYPE_STRING, description='Seed in hex format'),
            'private_key': openapi.Schema(type=openapi.TYPE_STRING, description='WIF private key'),
            'dogecoin_address': openapi.Schema(type=openapi.TYPE_STRING, description='Dogecoin address')
        }
    ))}
)
@api_view(['GET'])
def create_wallets_doge(request):
    mnemo = Mnemonic("english")
    phrase = mnemo.generate()
    seed = mnemo.to_seed(phrase)

    doge_network = Network('dogecoin')
    key = HDKey.from_seed(seed, network=doge_network)

    private_key = key.wif()
    dogecoin_address = key.address()

    data = {
        'mnemonic': phrase,
        'seed': seed.hex(),
        'private_key': private_key,
        'dogecoin_address': dogecoin_address
    }

    return JsonResponse(data)
