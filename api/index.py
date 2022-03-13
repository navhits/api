from fastapi import FastAPI, Depends, BackgroundTasks, File, UploadFile
from starlette.responses import Response, JSONResponse
from fastapi.responses import HTMLResponse, StreamingResponse

from api.auth import APIKeyAuth
from api.deta_base import pull_db, update_db, is_db_alive
from api.deta_drive import get_from_drive, put_to_drive
from api.firebase import get_storage_url
from api.schema import Info, Storage, StorageError, Drive, DriveError

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
    """
    Generic root endpoint
    """
    return Response(status_code=200)

@app.get("/health/api", tags=["Health"], responses={200: {"message": "Alive"}, 500: {"message": "Dead"}})
def api_health():
    """
    Endpoint to check if the API is alive
    """
    return JSONResponse(content={"message": "Alive"}, status_code=200)

@app.get("/health/db", tags=["Health"], responses={200: {"message": "Alive"}, 500: {"message": "Dead"}})
def db_health():
    """
    Endpoint to check if the DB is alive
    """
    if is_db_alive():
        return JSONResponse(content={"message": "Alive"}, status_code=200)
    return JSONResponse(content={"message": "Dead"}, status_code=500)

@app.get("/info", tags=["Info"], response_model=Info)
def read_my_info() -> dict:
    """
    Reads the database and returns the data
    """
    data = pull_db()
    data.pop("key")
    return JSONResponse(content=data, status_code=200)

@app.get("/info/refresh", tags=["info"], responses={202: {"message": "Accepted"}})
def refresh_my_info(background_tasks: BackgroundTasks, auth: str = Depends(AuthClass.authenticate)) -> dict:
    """
    Refreshes the database and returns the data
    """
    if auth:
        background_tasks.add_task(update_db)
        return Response(status_code=202)

@app.get("/storage", tags=["Storage"], responses={404: {"model": StorageError}, 200: {"model": Storage}})
def get_path_from_storage(path: str)  -> dict:
    """
    Get the path url for the requested item in the bucket
    """
    url = get_storage_url(path)
    if url:
        return JSONResponse(content={"url": url}, status_code=200)
    return JSONResponse(content={"error":"Path not found"}, status_code=404)

@app.post("/drive/upload", tags=["Drive"], responses={404: {"model": DriveError}, 200: {"model": Drive}})
def upload_to_drive(file: UploadFile = File(...)) -> dict:
    """
    Upload the file to the drive
    """
    name = file.filename
    f = file.file
    upload = put_to_drive(name, f)
    if upload:
        return JSONResponse(content={"url":f"https://api.navs.page/drive/download/{name}"}, status_code=200)
    return JSONResponse(content={"error":"Unable to upload"}, status_code=500)

@app.get("/drive/download/{name}", tags=["Drive"], responses={404: {"model": DriveError}})
def download_from_drive(name: str) -> StreamingResponse:
    """
    Downloads the file from drive
    """
    data = get_from_drive(name)
    if data:
        return StreamingResponse(data.iter_chunks(1024), media_type="application/pdf")
    return JSONResponse(content={"error":"File not found"}, status_code=404)
