import requests
from requests.auth import HTTPBasicAuth
import json
from urllib3.exceptions import InsecureRequestWarning
from urllib3 import disable_warnings
from dotenv import load_dotenv
import os

# Cargar las variables de ambiente desde el archivo dotenv_path="../../.env.academia"
load_dotenv(dotenv_path="../../.env.academia")

# Elimina los Warnings que salen en consola
disable_warnings(InsecureRequestWarning)

# Datos de autenticación
url = "https://192.168.56.11/restconf/data/ietf-interfaces:interfaces"
username = os.getenv("CSR_USERNAME")
password = os.getenv("CSR_PASSWORD")

# Encabezados HTTP
headers = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json",
}

# Enviar la solicitud HTTP PATCH para configurar la interfaz Loopback
response = requests.get(
    url,
    auth=HTTPBasicAuth(username, password),
    headers=headers,
    json={},
    verify=False,  # Desactivar la verificación de certificado (no recomendado en producción)
)

# Comprobamos el código de estado HTTP
if response.status_code >= 200 and response.status_code < 300:
    # El código de estado está en el rango 200-299, lo que indica una respuesta exitosa.
    response_dict = response.json()
    print(json.dumps(response_dict, indent=4))

else:
    # El código de estado está fuera del rango 200-299, lo que indica un error.
    print(f"Error. Código de estado HTTP: {response.status_code}")
