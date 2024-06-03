from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

"""
URL teste rota /weather/city/get_data:
    http://127.0.0.1:8000/api/v1/weather/city/get_data?city=Divinopolis&lang=pt-br


"""

@router.get("/weather/city/get_data", tags=["city"])
def api_get_city_data(city: str, lang: str):
    print(f'Cidade : {city}, Lingua: {lang}')
    return JSONResponse(
        status_code=200,
        content={"city" : city, "lang": lang},
        headers={"Success" : "Resquest successful"}
    )