from django.shortcuts import render
from django.http import JsonResponse
from mnemonic import Mnemonic
from bitcoinlib.keys import HDKey

def viewsnoid(request):
    mnemo = Mnemonic("english")
    phrase = mnemo.generate()
    seed = mnemo.to_seed(phrase)
    key = HDKey.from_seed(seed)
    public_key = key.wif()
    address = key.address()

    data = {
        'address': address
    }
    
    return JsonResponse(data)
    