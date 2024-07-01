from django.shortcuts import render
from django.http import JsonResponse
from mnemonic import Mnemonic
from bitcoinlib.keys import HDKey

def create_wallets_btc(request):
    # Criando carteira Bitcoin
    mnemo = Mnemonic("english")
    phrase = mnemo.generate()
    seed = mnemo.to_seed(phrase)
    key = HDKey.from_seed(seed)
    public_key = key.wif()
    bitcoin_address = key.address()

    data = {
        'bitcoin_address': bitcoin_address
    }

    return JsonResponse(data)

from bitcoinlib.networks import Network

def create_wallets_doge(request):
    # Criando carteira Dogecoin
    mnemo = Mnemonic("english")
    phrase = mnemo.generate()
    seed = mnemo.to_seed(phrase)

    # Configurar a rede Dogecoin
    doge_network = Network('dogecoin')
    key = HDKey.from_seed(seed, network=doge_network)

    dogecoin_address = key.address()

    data = {
        'dogecoin_address': dogecoin_address
    }

    return JsonResponse(data)