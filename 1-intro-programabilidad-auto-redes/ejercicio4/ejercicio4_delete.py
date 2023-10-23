# Se importa la librería para su uso
import requests
import json

# Nombre de Dispositivo a borrar
hostname = "Router3"

# Definimos y guardamos el URL del API REST
url = f"http://192.168.56.10:8000/api/router/{hostname}"

# Definimos el Payload de la consulta, como es GET se queda vacío
payload = {}

#  Se especifica el tipo de datos a enviar en el Payload(JSON)
headers = {"Authorization": "Basic dXNlcjE6cGFzc3dvcmQx"}

# Hacemos uso del método request() para ejecutar la llamada al API
response = requests.request("DELETE", url, headers=headers, data=payload)

# Comprobamos el código de estado HTTP
if response.status_code >= 200 and response.status_code < 300:
    # El código de estado está en el rango 200-299, lo que indica una respuesta exitosa.
    resp_dict = json.loads(response.text)
    print(
        f"Hostname: {resp_dict['hostname']}, IP Address: {resp_dict['ip_address']} . Eliminado exitosamente!"
    )
else:
    # El código de estado está fuera del rango 200-299, lo que indica un error.
    print("Error: HTTP Status Code", response.status_code)
