from netmiko import ConnectHandler

# Define a list of routers with their connection parameters
router = {
    "device_type": "cisco_xe",
    "ip": f"192.168.56.11",
    "username": "devnet",
    "password": "cisco",
}

# Configuration commands to be sent to each router
show_commands = "show interfaces"

try:
    # Connect to the router
    net_connect = ConnectHandler(**router)

    # Send configuration commands
    output = net_connect.send_command(show_commands)

    print(f"\nTipo Objecto: {type(output)}\n\nSalida:\n\n{output}\n")

    # Disconnect from the router
    net_connect.disconnect()

except Exception as e:
    print(f"Fallido en operar sobre {router['ip']} con error: {str(e)}")
