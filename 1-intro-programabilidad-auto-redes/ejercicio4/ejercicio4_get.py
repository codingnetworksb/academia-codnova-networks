# Se importa la librería para su uso
import requests
import json

# Definimos y guardamos el URL del API REST
url = "http://192.168.56.10:8000/api/router/"

# Definimos el Payload de la consulta, como es GET se queda vacío
payload = {}

# Definimos los Headers personalizados para la consulta, que para esta API puede ir vacío
headers = {}

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
