from fastapi import FastAPI
from starlette.responses import Response
from deta import Deta

import os

from firebase import firebase_app

app = FastAPI()
deta = Deta(project_key=os.getenv('DETA_PROJECT_KEY'))
db = deta.Base(os.getenv('FIREBASE_PROJECT_ID'))

@app.on_event("startup")
def startup():
    realtime_db = firebase_app.database()
    data = realtime_db.get()
    data = dict(data.val())
    data.update(key="1")
    db.put(data)
    
@app.on_event("shutdown")
def shutdown():
    pass

@app.get("/")
def root():
    return Response(status_code=200)

@app.get("/db")
def read_db():
    data = db.get(key="1")
    data.pop("key")
    return Response(content=data, status_code=200)
