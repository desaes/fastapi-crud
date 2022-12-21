# https://stackoverflow.com/questions/70535711/how-to-upload-both-file-and-json-data-using-fastapi

import requests
from fastapi import (APIRouter, Body, Depends, File, Form, Header,
                     HTTPException, Path, Query, Request, Response, UploadFile,
                     status)
from pydantic import BaseModel
from src.dtos.response import DetailResponse

router = APIRouter(prefix="/v1/movies", tags=["movies"])


class Base(BaseModel):
    item_type: int
    concept: int
    upload_type: int
    description: str
    is_public: bool
    validate_: bool


@router.post("/{movie_id}/file_with_json", response_model=DetailResponse)
async def post_file(
    request: Request,
    response: Response,
    movie_id: int = Path(default=..., description="Movie identifier"),
    base: Base = Depends(),
    file: UploadFile = File(...),
):

    try:
        received_data = base.dict()
        contents = file.file.read()
        with open("/tmp/" + file.filename, "wb") as f:
            f.write(contents)
    except Exception as e:
        return {"message": "There was an error uploading the file - " + e}
    finally:
        file.file.close()
    return DetailResponse(
        message=f"Movie id: {movie_id}, Item type: {received_data['item_type']}, Concept: {received_data['concept']}, Is public: {received_data['is_public']}, Filename: {file.filename}"
    )
