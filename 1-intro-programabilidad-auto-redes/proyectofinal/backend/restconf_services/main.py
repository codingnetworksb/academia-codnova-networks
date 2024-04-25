from fastapi import FastAPI
import requests
import os
import base64

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.get("/restconf/get-interfaces/{device_name}")
async def get_interfaces(device_name: str):
    """
    Obtiene la información de las interfaces del dispositivo a través de RESTCONF.
    """
    restconf_host = device_name
    restconf_port = os.environ.get("RESTCONF_PORT")
    restconf_username = os.environ.get("RESTCONF_USERNAME")
    restconf_password = os.environ.get("RESTCONF_PASSWORD")

    url = f"https://{restconf_host}:{restconf_port}/restconf/data/ietf-interfaces:interfaces"
    headers = {
        "Accept": "application/json",
        "Authorization": "Basic " + base64.b64encode((restconf_username + ":" + restconf_password).encode()).decode(),
    }

    response = requests.get(url, headers=headers, verify=False)
    return response.json()
