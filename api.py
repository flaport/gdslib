from typing import Annotated

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
import manage

app = FastAPI()


from fastapi import File, UploadFile

@app.post("/upload")
def upload(file: UploadFile = File(...)):
    try:
        manage.upload_file(file)
    except Exception as e:
        return {"message": "There was an error uploading the file", 'more info': str(e)}
    finally:
        file.file.close()

    return {"message": f"Successfully uploaded {file.filename}"}


@app.get("/")
def get_list():
    files = manage.get_list()
    return files


@app.get("/get/{filehash}")
def get_file(filehash: str):
    file_path = manage.get_file(filehash)
    if file_path is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return FileResponse(path=file_path, filename=file_path, media_type='text/text')

