from ncclient import manager

# Datos de autenticación
devices = ["192.168.56.11", "192.168.56.15"]
username = "codingnetworks"
password = "Coding.Networks1"

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
