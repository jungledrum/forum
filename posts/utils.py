from pymongo import MongoClient
from django.shortcuts import redirect


def init_db():
    client = MongoClient()
    return client.forum


def login_required(f):

    def decorator(request, *args, **kwargs):
        if request.session.get('username', None):
            return f(request, *args, **kwargs)
        else:
            return redirect('/users/new/')

    return decorator

SALT = '\x1f\xed\xf3"\x1c\xc0@\xc7\x91\xceXy\xef\xf3\xb3\xdb\r\xbf\x9e\xf3\xdcfZ\xf6'
