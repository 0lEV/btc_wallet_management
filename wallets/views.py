from django.shortcuts import render
from wallets.utils import successful_response, create_rpc_connection
import json


def index(request):
    return render(request, 'index.html')


def get_new_address(request):
    params = json.loads(request.body)
    rpc_connection = create_rpc_connection(params)
    res = rpc_connection.getnewaddress('')
    return successful_response(res)


def check_balance(request):
    params = json.loads(request.body)
    rpc_connection = create_rpc_connection(params)
    res = rpc_connection.getbalance('')
    return successful_response(res)


def get_addresses(request):
    params = json.loads(request.body)
    rpc_connection = create_rpc_connection(params)
    res = rpc_connection.getaddressesbyaccount('')
    return successful_response(res)





