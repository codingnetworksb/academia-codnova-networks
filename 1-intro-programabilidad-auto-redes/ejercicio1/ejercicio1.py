from netmiko import ConnectHandler

# Define a list of routers with their connection parameters
routers = []
for num in [5, 6, 11, 12]:
    routers.append(
        {
            "device_type": "cisco_ios",
            "ip": f"192.168.21.{num}",
            "username": "codingnetworks",
            "password": "coding21",
        },
    )

# Configuration commands to be sent to each router
config_commands = [
    "ip access-list extended SSH_MANAGEMENT",
    "permit ip 192.168.56.0 0.0.0.255 any",
    "permit ip 192.168.100.0 0.0.0.255 any",
]

# Loop through each router and configure it
for router in routers:
    try:
        # Connect to the router
        net_connect = ConnectHandler(**router)

        # Send configuration commands
        output = net_connect.send_config_set(config_commands)
        print(f"Configurando router {router['ip']}:\n{output}\n")

        # Disconnect from the router
        net_connect.disconnect()

    except Exception as e:
        print(
            f"Error al Configurar Router {router['ip']}. El error presentado fue: {str(e)}"
        )
