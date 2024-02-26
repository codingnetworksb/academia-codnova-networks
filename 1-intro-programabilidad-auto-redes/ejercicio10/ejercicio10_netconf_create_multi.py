from ncclient import manager
from dotenv import load_dotenv
import os

# Cargar las variables de ambiente desde el archivo dotenv_path="../.env.academia"
load_dotenv(dotenv_path="../.env.academia")

# Datos de autenticación
devices = ["192.168.56.11"]
username = os.getenv("CSR_USERNAME")
password = os.getenv("CSR_PASSWORD")

multi_loopbacks = ""
for num in range(100, 130):
    multi_loopbacks += f"""
            <interface>
                <name>Loopback{num}</name>
                <description>Interfaz Loopback</description>
                <type>ianaift:softwareLoopback</type>
                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                    <address>
                        <ip>192.168.1.{num}</ip>
                        <netmask>255.255.255.255</netmask>
                    </address>
                </ipv4>
            </interface>
    """

# Crear una conexión SSH NETCONF
for hostname in devices:
    with manager.connect(
        host=hostname,
        username=username,
        password=password,
        device_params={"name": "csr"},
    ) as m:
        loopback_config = f"""
        <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
            <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                {multi_loopbacks}
            </interfaces>
        </config>

        """
        print(loopback_config)
        # Ejecución de la configuración
        m.edit_config(target="candidate", config=loopback_config)

        m.commit()
