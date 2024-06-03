from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.api.services.openWeather import get_weather_data

router = APIRouter()

"""
URL teste rota /weather/city/get_data:
    http://127.0.0.1:8000/api/v1/weather/city/get_data?city=Divinopolis&lang=pt-br


"""

@router.get("/weather/city/get_data", tags=["city"])
def api_get_city_data(city: str, lang: str):
    weatherJson = get_weather_data(city,lang)
    if 'error' in weatherJson:
        return JSONResponse(
            status_code=weatherJson.get('status', 500),
            content=weatherJson['error'],
            headers={"X-Error": "There was an error with the request"}
        )
    else:
        return weatherJson