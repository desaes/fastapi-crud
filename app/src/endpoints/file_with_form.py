# https://stackoverflow.com/questions/70535711/how-to-upload-both-file-and-json-data-using-fastapi

import requests
from fastapi import (APIRouter, Body, Depends, File, Form, Header,
                     HTTPException, Path, Query, Request, Response, UploadFile,
                     status)
from src.dtos.response import DetailResponse

router = APIRouter(prefix="/v1/movies", tags=["movies"])


@router.post("/{movie_id}/file_with_form", response_model=DetailResponse)
async def post_file(
    request: Request,
    response: Response,
    movie_id: int = Path(default=..., description="Aranda ticket identifier"),
    item_type: int = Form(...),
    concept: int = Form(...),
    upload_type: int = Form(...),
    description: str = Form(...),
    is_public: bool = Form(...),
    validate: bool = Form(...),
    file: UploadFile = File(...),
):
    try:
        contents = file.file.read()
        with open("/tmp/" + file.filename, "wb") as f:
            f.write(contents)
    except Exception as e:
        return {"message": "There was an error uploading the file - " + e}
    finally:
        file.file.close()
    return DetailResponse(
        message=f"Movie id: {movie_id}, Item type: {item_type}, Concept: {concept}, Is public: {is_public}, Filename: {file.filename}"
    )
