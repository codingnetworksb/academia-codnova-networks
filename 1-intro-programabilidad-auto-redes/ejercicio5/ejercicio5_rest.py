import requests
import json
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings

# Elimina los Warnings que salen en consola
disable_warnings(InsecureRequestWarning)

# URL para obtener Token de autenticación
url = "https://192.168.56.11:55443/api/v1/auth/token-services"

headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Basic ZGV2bmV0OmNpc2Nv",
}

response = requests.request("POST", url, headers=headers, data={}, verify=False)

token_data = response.json()

url = "https://192.168.56.11:55443/api/v1/interfaces"

payload = {}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "X-auth-token": token_data["token-id"],
}

response = requests.get(url, headers=headers, verify=False)

# Comprobamos el código de estado HTTP
if response.status_code >= 200 and response.status_code < 300:
    # El código de estado está en el rango 200-299, lo que indica una respuesta exitosa.

    # Convierte a diccionario
    response_dict = response.json()

    print(f"\nTipo Objecto: {type(response_dict)}\n\nSalida:\n\n")
    print(json.dumps(response_dict, indent=4))

else:
    # El código de estado está fuera del rango 200-299, lo que indica un error.
    print("Error: HTTP Status Code", response.status_code)
