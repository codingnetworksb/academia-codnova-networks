from fastapi import FastAPI
from csr_service import csr_client

app = FastAPI()
username = "codingnetworks"
password = "coding21"
base_url = "https://192.168.56.11:55443/api/v1/"
csr_router = csr_client.CSRClient(username, password, base_url)


@app.get("/interfaces")
def get_interfaces():
    return csr_router.get_interfaces()


# ...Add routes for other operations
