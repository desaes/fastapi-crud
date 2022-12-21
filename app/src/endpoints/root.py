from fastapi import (APIRouter, Body, Depends, Header, HTTPException, Path,
                     Query)
from src.dtos.response import DetailResponse

router = APIRouter(prefix="/v1/movies", tags=["movies"])


@router.get("/", response_model=DetailResponse)
async def get_root():
    return DetailResponse(message=f"Hello World")
