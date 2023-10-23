# Se importan las librerías a utilizar
import requests
import json

# Se define y guarda el URL del API REST
url = "http://192.168.56.10:8000/api/router/"

# Construimos el Payload/Body con los datos a insertar
payload = json.dumps(
    {"hostname": "Router3", "ip_address": "192.168.56.103", "vendor": "Cisco"}
)
#  Se especifica el tipo de datos a enviar en el Payload(JSON)
headers = {"Content-Type": "application/json"}

# Se ejecuta el método requests() para realizar la llamada POST al API REST
response = requests.request("POST", url, headers=headers, data=payload)

# Comprobamos el código de estado HTTP
if response.status_code >= 200 and response.status_code < 300:
    # El código de estado está en el rango 200-299, lo que indica una respuesta exitosa.

    resp_dict = json.loads(response.text)
    print(
        f"Hostname: {resp_dict['hostname']}, IP Address: {resp_dict['ip_address']} . Agregado exitosamente!"
    )
else:
    # El código de estado está fuera del rango 200-299, lo que indica un error.
    print("Error: HTTP Status Code", response.status_code)
