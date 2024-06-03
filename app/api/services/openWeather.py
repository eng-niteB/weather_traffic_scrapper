import os
import requests
from app.utils.config import load_env_variables
from typing import Dict, Any

def get_weather_data(city : str, lang: str) -> Dict[str, Any] :
    """
    Busca os dados a partir de uma determinada cidade
    
    Parametros:
    city (str): Cidade de onde se deseja buscar as informacoes de clima.
    lang (str): A linguagem que deseja nas descrições do clima.

    Retorno:
    dict: As informações de clima em caso de sucesso e um array vazio em caso de falha.
    """
    
    weather_key = os.getenv('WEATHER_KEY')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}&lang={lang}"
    print(url)
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return {'status': response.status_code, 'error': str(http_err)}
    except requests.exceptions.RequestException as req_err:
        return {'status': 'Request Error', 'error': str(req_err)}
    except Exception as err:
        return {'status': 'Error', 'error': str(err)}
    
# Load enviroment variables
load_env_variables()