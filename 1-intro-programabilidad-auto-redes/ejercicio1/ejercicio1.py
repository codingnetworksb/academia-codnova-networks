from netmiko import ConnectHandler
from dotenv import load_dotenv
import os

# Cargar las variables de ambiente desde el archivo dotenv_path="../../.env.academia"
load_dotenv(dotenv_path="../../.env.academia")

# Definir una lista de routers con sus parámetros de conexión.
routers = []
for num in [5, 6, 11, 12]:
    routers.append(
        {
            "device_type": "cisco_xe",
            "ip": f"192.168.21.{num}",
            "username": os.getenv("CSR_USERNAME"),
            "password": os.getenv("CSR_PASSWORD"),
        },
    )

# Comandos de configuración que se enviarán a cada router
config_commands = [
    "ip access-list extended SSH_MANAGEMENT",
    "permit ip 192.168.56.0 0.0.0.255 any",
    "permit ip 192.168.100.0 0.0.0.255 any",
]

# Recorre cada router y configúrelo
for router in routers:
    try:
        # Conectate al router
        net_connect = ConnectHandler(**router)

        # Envía los comandos de configuración
        output = net_connect.send_config_set(config_commands)
        print(f"Configurando router {router['ip']}:\n{output}\n")

        # Desconectate del router
        net_connect.disconnect()

    except Exception as e:
        print(
            f"Error al Configurar Router {router['ip']}. El error presentado fue: {str(e)}"
        )
