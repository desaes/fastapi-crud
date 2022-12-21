# https://stackoverflow.com/questions/70535711/how-to-upload-both-file-and-json-data-using-fastapi

from typing import List

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


@router.post("/{movie_id}/files_with_json", response_model=DetailResponse)
async def post_file(
    request: Request,
    response: Response,
    movie_id: int = Path(default=..., description="Movie identifier"),
    base: Base = Depends(),
    files: List[UploadFile] = File(...),
):

    try:
        received_data = base.dict()
        for file in files:
            contents = file.file.read()
            with open("/tmp/" + file.filename, "wb") as f:
                f.write(contents)
    except Exception as e:
        return {
            "message": f"There was an error uploading the file {file.filename} - " + e
        }
    finally:
        file.file.close()
    return DetailResponse(
        message=f"Movie id: {movie_id}, Item type: {received_data['item_type']}, Concept: {received_data['concept']}, Is public: {received_data['is_public']}, Filenames: {[file.filename for file in files]}"
    )
