from fastapi import FastAPI
from netmiko import ConnectHandler
import os

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.post("/netmiko/send-command/{device_name}")
async def send_command(device_name: str, command: str):
    """
    Envía un comando al dispositivo a través de SSH con NETMIKO.
    """
    netmiko_device = {
        "device_type": "cisco_ios",
        "host": device_name,
        "username": os.environ.get("NETMIKO_USERNAME"),
        "password": os.environ.get("NETMIKO_PASSWORD"),
    }

    with ConnectHandler(**netmiko_device) as device_conn:
        result = device_conn.send_command(command)

    return {"result": result}
