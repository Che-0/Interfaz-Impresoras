from bs4 import BeautifulSoup
import requests


def analizar_pagina_web(url):
  # Cabeceras para simular un navegador web
  headers = {
      "User-Agent": (
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,"
          " like Gecko) Chrome/120.0.0.0 Safari/537.36"
      )
  }

  try:
    # 1. Realizar la petición HTTP
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    print(response.text)

    # 2. Parsear el contenido HTML con BeautifulSoup
    # Usamos 'html.parser' que viene por defecto en Python
    soup = BeautifulSoup(response.text, "html.parser")

    return soup

  except requests.exceptions.HTTPError as http_err:
    print(f"Error HTTP: {http_err}")
  except requests.exceptions.ConnectionError as conn_err:
    print(f"Error de conexión: {conn_err}")
  except requests.exceptions.Timeout as timeout_err:
    print(f"La petición ha expirado: {timeout_err}")
  except requests.exceptions.RequestException as err:
    print(f"Ocurrió un error inesperado: {err}")

  return None


if __name__ == "__main__":
  # URL de ejemplo (puedes cambiarla por la que necesites)
  url_objetivo = "http://10.60.32.23/webglue/rawcontent?timedRefresh=1&c=Status&lang=es"



  print(f"Analizando la página: {url_objetivo}...\n")
  soup = analizar_pagina_web(url_objetivo)

  if soup:
    # --- EJEMPLOS DE CÓMO EXTRAER INFORMACIÓN LEGIBLE ---

    # 1. Obtener el título de la pestaña de la página
    titulo_pagina = soup.title.string if soup.title else "Sin título"
    print(f"Título de la página: {titulo_pagina}\n")

    # 2. Extraer el texto limpio (eliminando todas las etiquetas HTML)
    # .get_text() extrae todo el texto plano legible
    texto_limpio = soup.get_text(separator="\n", strip=True)
    print("--- Primeros 400 caracteres del texto legible ---")
    #print(texto_limpio)

    # 3. Ejemplo de cómo buscar elementos específicos (por ejemplo, todos los encabezados <h1>)
    print("\n--- Encabezados H1 encontrados ---")
    h1_tags = soup.find_all("h1")
    if h1_tags:
      for h1 in h1_tags:
        print(f"- {h1.get_text(strip=True)}")
    else:
      print("No se encontraron etiquetas H1.")

    # 4. Ejemplo de cómo buscar enlaces (etiquetas <a>)
    print("\n--- Primeros 3 enlaces encontrados ---")
    enlaces = soup.find_all("a", limit=3)
    for a in enlaces:
      texto_enlace = a.get_text(strip=True)
      url_enlace = a.get("href")
      print(f"- Texto: '{texto_enlace}' | URL: {url_enlace}")

#http://10.60.32.23/webglue/rawcontent?timedRefresh=1&c=Status&lang=es
#Regresa en json los datos 
#supplies {
#  "Black Toner": cartucho negro 
#  "Black Imaging Kit" unidad 
#  "Maintenance Kit":
#}
