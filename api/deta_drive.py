import os

from deta import Deta


deta = Deta(project_key=os.getenv('DETA_PROJECT_KEY'))

def get_from_drive(name):
    drive = deta.Drive("static")
    try:
        data = drive.get(name=name)
        return data
    except Exception:
        return None

def put_to_drive(name, data):
    drive = deta.Drive("static")
    try:
        drive.put(name=name, data=data)
        return True
    except Exception:
        return False
