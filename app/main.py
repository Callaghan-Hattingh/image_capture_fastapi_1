import uvicorn
from fastapi import FastAPI
from app.api.api import api_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(api_router, prefix="/api")
# app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, workers=1)
