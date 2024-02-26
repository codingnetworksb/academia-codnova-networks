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
    loopback_config = """
    <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>Loopback155</name>
                <description>Interfaz Loopback</description>
                <type>ianaift:softwareLoopback</type>
                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                    <address>
                        <ip>192.168.1.1</ip>
                        <netmask>255.255.255.255</netmask>
                    </address>
                </ipv4>
            </interface>
        </interfaces>
    </config>

    """
    # Ejecución de la configuración
    m.edit_config(target="candidate", config=loopback_config)

    m.commit()
