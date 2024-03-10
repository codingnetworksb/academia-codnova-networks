from ncclient import manager
from dotenv import load_dotenv
import os

# Cargar las variables de ambiente desde el archivo dotenv_path="../../.env.academia"
load_dotenv(dotenv_path="../../.env.academia")

# Datos de autenticación
devices = ["192.168.56.11", "192.168.56.12"]
username = os.getenv("CSR_USERNAME")
password = os.getenv("CSR_PASSWORD")

multi_loopbacks = ""
for num in range(100, 130):
    multi_loopbacks += f"""
            <interface operation="delete">
                <name>Loopback{num}</name>
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
        # Dentro de la sesión NETCONF
        loopback_delete = f"""
        <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
            <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                {multi_loopbacks}
            </interfaces>
        </config>
        """
        print(loopback_delete)
        m.edit_config(target="candidate", config=loopback_delete)
        m.commit()
