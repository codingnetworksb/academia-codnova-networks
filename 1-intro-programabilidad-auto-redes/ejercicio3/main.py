from typing import List
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel

app = FastAPI()
security = HTTPBasic()

# Simulación de almacenamiento de usuarios permitidos (reemplaza con tu propio almacenamiento)
allowed_users = {
    "user1": {"password": "password1"},
    "user2": {"password": "password2"},
}


class RouterData(BaseModel):
    hostname: str
    ip_address: str
    vendor: str


router_data_db = []


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
