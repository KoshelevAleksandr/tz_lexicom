import uvicorn
from fastapi import FastAPI, APIRouter

from api.schemas import WriteData, CheckDataResponse

from api.handlers import data_router

app = FastAPI(
    title="tz_Lexicom"
)

main_api_router = APIRouter()

main_api_router.include_router(data_router)
app.include_router(main_api_router)


@app.get("/")
async def main_get():
    return "Hello"


if __name__ == "__main__":
    # run app on the host and port
    uvicorn.run(app, host="localhost", port=8000)
