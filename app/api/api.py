from fastapi import FastAPI
from api.routes import weather

app = FastAPI()

app.include_router(weather.router, prefix='/api/v1')