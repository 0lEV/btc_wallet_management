from django.shortcuts import render
from wallets.utils import success_response, error_response, create_rpc_connection
from bitcoinrpc.authproxy import JSONRPCException
import json


def index(request):
    return render(request, 'index.html')


def get_new_address(request):
    params = json.loads(request.body)
    rpc_connection = create_rpc_connection(params)
    try:
        res = rpc_connection.getnewaddress('')
        return success_response(res)
    except JSONRPCException as e:
        msg = 'Error: ' + e.message
        return error_response(msg)



def check_balance(request):
    params = json.loads(request.body)
    rpc_connection = create_rpc_connection(params)
    try:
        res = rpc_connection.getbalance('')
        return success_response(res)
    except JSONRPCException as e:
        msg = 'Error: ' + e.message
        return error_response(msg)


def get_addresses(request):
    params = json.loads(request.body)
    rpc_connection = create_rpc_connection(params)
    try:
        res = rpc_connection.getaddressesbyaccount('')
        return success_response(res)
    except JSONRPCException as e:
        msg = 'Error: ' + e.message
        return error_response(msg)





