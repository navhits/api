from fastapi import FastAPI, Depends, BackgroundTasks
from starlette.responses import Response, JSONResponse

from api.auth import APIKeyAuth
from api.deta_base import pull_db, update_db
from api.firebase import get_storage_url
from api.schema import Info, Storage, StorageError

app = FastAPI(
    title="Naveen's API",
    description="You can now view my profile with an API call",
    version="0.0.1",
    contact={
        "name": "Naveen S",
        "url": "https://navs.page",
        "email": "dev@navs.page",
    },
    )
AuthClass = APIKeyAuth()

@app.on_event("startup")
def startup():
    pull_db()
    
@app.on_event("shutdown")
def shutdown():
    pass

@app.get("/")
def root():
    return Response(status_code=200)

@app.get("/info", tags=["Info"], response_model=Info)
def read_my_info() -> dict:
    """
    Reads the database and returns the data
    """
    data = pull_db()
    data.pop("key")
    return JSONResponse(content=data, status_code=200)

@app.get("/info/refresh", tags=["info"], response_model=Info)
def refresh_my_info(background_tasks: BackgroundTasks, auth: str = Depends(AuthClass.authenticate)) -> dict:
    """
    Refreshes the database and returns the data
    """
    if auth:
        background_tasks.add_task(update_db)
        return JSONResponse(status_code=202)

@app.get("/storage", tags=["Storage"], responses={404: {"model": StorageError}, 200: {"model": Storage}})
def get_path_from_storage(path: str)  -> dict:
    """
    Get the path url for the requested item in the bucket
    """
    url = get_storage_url(path)
    if url:
        return JSONResponse(content={"url": url}, status_code=200)
    return JSONResponse(content={"error":"Path not found"}, status_code=404)
