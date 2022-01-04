import firebase_admin as firebase
from firebase_admin import db, storage
from api.config import config

cred = firebase.credentials.Certificate(config['serviceAccount'])
app = firebase.initialize_app(cred, config['options'], config['options']['projectId'])

def get_from_realtimedb():
    realtime_db = db.reference(path='/', app=app)
    data = realtime_db.get()
    return data

def get_storage_url(path):
    bucket = storage.bucket(app=app)
    blob = bucket.get_blob(path)
    if blob:
        blob.make_public()
        return blob.public_url
    return None
