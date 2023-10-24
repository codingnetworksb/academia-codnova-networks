from ncclient import manager

# Datos de autenticación
hostname = "192.168.56.11"
username = "codingnetworks"
password = "Coding.Networks1"

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
