import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os

# Cargar las variables de ambiente desde el archivo ".env.academia"
load_dotenv(".env.academia")

# Datos de autenticación
url = "https://192.168.56.11/restconf/data/ietf-interfaces:interfaces/interface=Loopback155"
username = os.getenv("CSR_USERNAME")
password = os.getenv("CSR_PASSWORD")

# Encabezados HTTP
headers = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json",
}

# Enviar la solicitud HTTP DELETE para configurar la interfaz Loopback
response = requests.delete(
    url,
    auth=HTTPBasicAuth(username, password),
    headers=headers,
    json={},
    verify=False,  # Desactivar la verificación de certificado (no recomendado en producción)
)

# Comprobamos el código de estado HTTP
if response.status_code >= 200 and response.status_code < 300:
    # El código de estado está en el rango 200-299, lo que indica una respuesta exitosa.
    print("Interfaz Loopback eliminada con éxito.")
else:
    # El código de estado está fuera del rango 200-299, lo que indica un error.
    print(f"Error en la configuración. Código de estado HTTP: {response.status_code}")
