from ncclient import manager

# Datos de autenticación
hostname = "192.168.56.11"
username = "codingnetworks"
password = "coding21"

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
