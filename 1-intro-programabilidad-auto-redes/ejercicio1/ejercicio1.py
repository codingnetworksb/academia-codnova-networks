from netmiko import ConnectHandler

# Define a list of routers with their connection parameters
routers = []
for num in range(1, 20):
    routers.append(
        {
            "device_type": "cisco_ios",
            "ip": f"192.168.21.{num}",
            "username": "codingnetworks",
            "password": "Coding.Networks1",
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
        print(f"Configuring {router['ip']}:\n{output}\n")

        # Disconnect from the router
        net_connect.disconnect()

    except Exception as e:
        print(f"Failed to configure {router['ip']} with error: {str(e)}")
