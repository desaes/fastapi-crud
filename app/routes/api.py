from fastapi import APIRouter

router = APIRouter()

from src.endpoints import file_with_form as file_with_form
from src.endpoints import file_with_json as file_with_json
from src.endpoints import files_with_form as files_with_form
from src.endpoints import files_with_json as files_with_json
from src.endpoints import root as root

router.include_router(root.router)
router.include_router(file_with_form.router)
router.include_router(files_with_form.router)
router.include_router(file_with_json.router)
router.include_router(files_with_json.router)
