from typing import List
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Cargar las variables de ambiente desde el archivo dotenv_path="../../.env.academia"
load_dotenv(dotenv_path=".env.academia")

app = FastAPI()
security = HTTPBasic()

# Simulación de almacenamiento de usuarios permitidos (reemplaza con tu propio almacenamiento)
allowed_users = {
    os.getenv("CSR_USERNAME"): {"password": os.getenv("CSR_PASSWORD")},
    "user2": {"password": "password2"},
}


class RouterData(BaseModel):
    hostname: str
    ip_address: str
    vendor: str


initial_entry = RouterData.parse_obj(
    {"hostname": "Router1", "ip_address": "192.168.56.101", "vendor": "Cisco"}
)
router_data_db = [initial_entry]


@app.post("/api/router/", response_model=RouterData)
def create_router_data(data: RouterData):
    router_data_db.append(data)
    return data


@app.get("/api/router/", response_model=List[RouterData])
def read_router_data():
    return router_data_db


# Función para verificar las credenciales del usuario
def verify_user(credentials: HTTPBasicCredentials = Depends(security)):
    user = allowed_users.get(credentials.username)
    if user is None or user["password"] != credentials.password:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized",
        )
    return user


@app.get("/api/protected-router/", response_model=List[RouterData])
async def read_protected_router_data(user: dict = Depends(verify_user)):
    return router_data_db


@app.delete("/api/router/{hostname}/")
def delete_router_data(hostname: str, user: dict = Depends(verify_user)):
    for router in router_data_db:
        if router.hostname == hostname:
            router_data_db.remove(router)
            return router
    raise HTTPException(
        status_code=404,
        detail=f"Router with hostname '{hostname}' not found",
    )
