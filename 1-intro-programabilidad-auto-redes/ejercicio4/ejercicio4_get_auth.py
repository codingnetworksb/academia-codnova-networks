# Se importa las librería a utilizar
import requests
import json

# Se define y guarda el URL del API REST
url = "http://192.168.56.10:8000/api/protected-router/"

# Definimos el Payload de la consulta, como es GET se queda vacío
payload = {}

# Definimos el header de autorización
headers = {"Authorization": "Basic dXNlcjE6cGFzc3dvcmQx"}

# Hacemos uso del método request() para ejecutar la llamada al API
response = requests.request("GET", url, headers=headers, data=payload)

# Comprobamos el código de estado HTTP
if response.status_code >= 200 and response.status_code < 300:
    # El código de estado está en el rango 200-299, lo que indica una respuesta exitosa.

    response_list = json.loads(response.text)

    for resp in response_list:
        print(f"Hostname: {resp['hostname']}, IP Address: {resp['ip_address']}")
else:
    # El código de estado está fuera del rango 200-299, lo que indica un error.
    print("Error: HTTP Status Code", response.status_code)
