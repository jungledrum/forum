from pymongo import MongoClient

def init_db():
    client = MongoClient()
    return client.forum

def is_login(request):
    if request.session.get('username', None):
        return True
    else:
        return False

SALT = '\x1f\xed\xf3"\x1c\xc0@\xc7\x91\xceXy\xef\xf3\xb3\xdb\r\xbf\x9e\xf3\xdcfZ\xf6'
