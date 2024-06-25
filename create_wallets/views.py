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
