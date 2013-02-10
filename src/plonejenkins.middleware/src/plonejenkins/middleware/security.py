# -*- encoding: utf-8 -*-

from pyramid.decorator import reify
from pyramid.request import Request


def validatejenkins(fn):
    def wrapped(request):
        # We check if the call is from jenkins server
        # import pdb; pdb.set_trace()
        token = request.token
        if token == request.registry.settings['api_key']:
            return fn(request)
        else:
            return {'success': False, 'message': 'Token not active'}
    return wrapped


def validatetoken(fn):
    def wrapped(request):
        token = request.token
        if token == request.registry.settings['api_key']:
            return fn(request)
        else:
            return {'success': False, 'message': 'Token not active'}
    return wrapped


class RequestWithAttributes(Request):

    @reify
    def token(self):
        if 'token' in self.GET:
            return self.GET['token']

    @reify
    def core(self):
        return self.registry.settings['core']

