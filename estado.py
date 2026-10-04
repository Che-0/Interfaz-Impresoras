import requests

'''
Esta función obtiene el estado de una impresora a partir de su URL.
Parámetros:
- url: La URL de la impresora.
Retorna:
- Un diccionario con el estado de la impresora o None si ocurre un error.
'''


def obtener_estado_impresora(url):
    # Cabeceras para simular un navegador o cliente HTTP válido
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
            " like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ),
        "Accept": "application/json, text/javascript, */*; q=0.01",
    }

    try:
        # 1. Realizar la petición HTTP
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # 2. Como la respuesta es un JSON, la convertimos directamente a diccionario de Python
        data = response.json()
        return data

    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error de conexión: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"La petición ha expirado: {timeout_err}")
    except ValueError as json_err:
        print(f"Error al decodificar el JSON: {json_err}")
    except requests.exceptions.RequestException as err:
        print(f"Ocurrió un error inesperado: {err}")

    return None
