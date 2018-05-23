from django.http import HttpResponse, JsonResponse
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException


def create_rpc_connection(params):
    username = params.get('username')
    password = params.get('password')
    server = params.get('server')
    return AuthServiceProxy("http://%s:%s@%s" % (username, password, server))


def make_response(data=None, error=''):
    return JsonResponse({'data': data, 'error': error})


def success_response(data):
    return make_response(data)


def error_response(error: str):
    return make_response(error=error)