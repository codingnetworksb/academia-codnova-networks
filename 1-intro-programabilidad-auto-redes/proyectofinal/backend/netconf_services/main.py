from fastapi import FastAPI
from ncclient import manager
import os

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.get("/api/devices")
async def devices():
    return [{"id": 1, "name": "CSR-1", "ip_address": "192.168.56.11"}]


@app.get("/netconf/get-config/{device_name}")
async def get_config(device_name: str):
    """
    Obtiene la configuración del dispositivo a través de NETCONF.
    """
    with manager.connect(
        host=device_name,
        port=os.environ.get("NETCONF_PORT"),
        username=os.environ.get("NETCONF_USERNAME"),
        password=os.environ.get("NETCONF_PASSWORD"),
        hostkey_verify=False,
    ) as m:
        return m.get_config(source="running").data_xml
