import requests
import pyrebase
from api.config import config

firebase_app = pyrebase.initialize_app(config)

def get_from_realtimedb():
    realtime_db = firebase_app.database()
    data = realtime_db.get()
    return dict(data.val())

def get_storage_url(path):
    storage = firebase_app.storage()
    data = storage.child(str(path))
    url = data.get_url(token=None)
    if verify_content(url):
        return url
    return None

def verify_content(url):
    res = requests.get(url)
    if res.status_code == 200:
        return True
    return False