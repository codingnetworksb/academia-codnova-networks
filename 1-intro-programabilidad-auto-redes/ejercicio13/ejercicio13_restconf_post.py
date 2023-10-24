import requests
from requests.auth import HTTPBasicAuth

# Datos de autenticación
url = "https://192.168.56.11/restconf/data/ietf-interfaces:interfaces"
username = "codingnetworks"
password = "Coding.Networks1"

# Encabezados HTTP
headers = {
    "Content-Type": "application/yang-data+json",
    "Accept": "application/yang-data+json",
}

# Datos de configuración
config_data = {
    "ietf-interfaces:interface": {
        "name": "Loopback155",
        "description": "Interfaz Loopback",
        "type": "iana-if-type:softwareLoopback",
        "ietf-ip:ipv4": {
            "address": [{"ip": "192.168.1.1", "netmask": "255.255.255.255"}]
        },
    }
}

# Enviar la solicitud HTTP POST para configurar la interfaz Loopback
response = requests.post(
    url,
    auth=HTTPBasicAuth(username, password),
    headers=headers,
    json=config_data,
    verify=False,  # Desactivar la verificación de certificado (no recomendado en producción)
)

# Comprobamos el código de estado HTTP
if response.status_code >= 200 and response.status_code < 300:
    # El código de estado está en el rango 200-299, lo que indica una respuesta exitosa.
    print("Interfaz Loopback configurada con éxito.")
else:
    # El código de estado está fuera del rango 200-299, lo que indica un error.
    print(f"Error en la configuración. Código de estado HTTP: {response.status_code}")
