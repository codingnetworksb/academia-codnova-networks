from fastapi import FastAPI
import napalm
import os

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.get("/napalm/get-facts/{device_name}")
async def get_facts(device_name: str):
    """
    Obtiene información general del dispositivo a través de NAPALM.
    """

    napalm_driver = os.environ.get("NAPALM_DRIVER")
    napalm_hostname = device_name
    napalm_username = os.environ.get("NAPALM_USERNAME")
    napalm_password = os.environ.get("NAPALM_PASSWORD")

    with napalm.get_network_driver(napalm_driver)(
        hostname=napalm_hostname, username=napalm_username, password=napalm_password
    ) as device:
        return device.get_facts()
