from fastapi import FastAPI, APIRouter

from api.handlers import data_router

app = FastAPI(
    title="tz_Lexicom"
)

main_api_router = APIRouter()

main_api_router.include_router(data_router)
app.include_router(main_api_router)
