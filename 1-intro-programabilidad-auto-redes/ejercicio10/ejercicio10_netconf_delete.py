from ncclient import manager
from dotenv import load_dotenv
import os

# Cargar las variables de ambiente desde el archivo ".env.academia"
load_dotenv(".env.academia")

# Datos de autenticación
hostname = "192.168.56.11"
username = os.getenv("CSR_USERNAME")
password = os.getenv("CSR_PASSWORD")

# Crear una conexión SSH NETCONF
with manager.connect(
    host=hostname,
    username=username,
    password=password,
    device_params={"name": "csr"},
) as m:
    # Dentro de la sesión NETCONF
    loopback_delete = """
    <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface operation="delete">
                <name>Loopback155</name>
            </interface>
        </interfaces>
    </config>
    """

    m.edit_config(target="candidate", config=loopback_delete)
    m.commit()
