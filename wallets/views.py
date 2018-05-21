from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
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



def create_rpc_connection(params):
    username = params.get('username')
    password = params.get('password')
    server = params.get('server')
    return AuthServiceProxy("http://%s:%s@%s" % (username, password, server))

def successful_response(data):
    return JsonResponse({'data': data})

