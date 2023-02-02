from fastapi import APIRouter

from .predict import predict_router


router: APIRouter = APIRouter(prefix="/api")
router.include_router(predict_router)
