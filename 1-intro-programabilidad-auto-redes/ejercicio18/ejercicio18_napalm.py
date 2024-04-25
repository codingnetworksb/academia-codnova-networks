import napalm
from dotenv import load_dotenv
import os

# Cargar las variables de ambiente desde el archivo dotenv_path="../../.env.academia"
load_dotenv(dotenv_path="../../.env.academia")

# Define los detalles de conexión para una lista de dispositivos
devices = [
    {
        "device_type": "ios",
        "hostname": "192.168.56.11",
        "username": os.getenv("CSR_USERNAME"),
        "password": os.getenv("CSR_PASSWORD"),
    },
    {
        "device_type": "ios",
        "hostname": "192.168.56.12",
        "username": os.getenv("CSR_USERNAME"),
        "password": os.getenv("CSR_PASSWORD"),
    },
]

# Itera a través de la lista de dispositivos
for device_info in devices:
    # Crea una instancia de NAPALM para el dispositivo
    driver = napalm.get_network_driver(device_info["device_type"])
    device = driver(
        hostname=device_info["hostname"],
        username=device_info["username"],
        password=device_info["password"],
    )

    try:
        # Conecta al dispositivo
        device.open()

        # Recupera información de las interfaces
        interfaces = device.get_interfaces()

        # Imprime las interfaces que están arriba junto con su descripción
        print(
            f"Información de interfaces en {device_info['hostname']} ({device_info['device_type']}):"
        )
        for interface, details in interfaces.items():
            if details.get("is_up"):
                print(
                    f"Interfaz: {interface}, Descripción: {details.get('description', 'Sin descripción')}"
                )

    except Exception as e:
        print(f"Error al conectar con {device_info['hostname']}: {str(e)}")
    finally:
        # Cierra la conexión al dispositivo
        device.close()
