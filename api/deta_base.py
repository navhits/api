from datetime import datetime, timedelta
import time, os

from deta import Deta

from api.firebase import get_from_realtimedb

deta = Deta(project_key=os.getenv('DETA_PROJECT_KEY'))


def is_db_alive():
    db = deta.Base(os.getenv('FIREBASE_PROJECT_ID'))
    data = db.get(key="1")
    if data:
        return True
    return False

def pull_db():
    db = deta.Base(os.getenv('FIREBASE_PROJECT_ID'))
    data = db.get(key="1")
    if data:
        timestamp = data.get("timestamp")
        if timestamp:
            if datetime.fromtimestamp(timestamp) > datetime.utcnow() - timedelta(hours=24):
                data = get_from_realtimedb()
                data.update(key="1", timestamp=time.time())
                db.put(data)
    else:
        data = get_from_realtimedb()
        data.update(key="1", timestamp=time.time())
        db.put(data)
    return data

def update_db():
    db = deta.Base(os.getenv('FIREBASE_PROJECT_ID'))
    data = get_from_realtimedb()
    data.update(key="1", timestamp=time.time())
    db.put(data)
    return data
