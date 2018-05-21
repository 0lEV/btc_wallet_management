from django.http import HttpResponse, JsonResponse
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException


def create_rpc_connection(params):
    username = params.get('username')
    password = params.get('password')
    server = params.get('server')
    return AuthServiceProxy("http://%s:%s@%s" % (username, password, server))

def successful_response(data):
    return JsonResponse({'data': data})