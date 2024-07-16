from bitcoinlib.networks import Network
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
    private_key = key.wif()
    bitcoin_address = key.address()

    data = {
        'mnemonic': phrase,
        'seed': seed.hex(),
        'private_key': private_key,
        'bitcoin_address': bitcoin_address
    }

    return JsonResponse(data)

def create_wallets_doge(request):
    # Criando carteira Dogecoin
    mnemo = Mnemonic("english")
    phrase = mnemo.generate()
    seed = mnemo.to_seed(phrase)

    # Configurar a rede Dogecoin
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
