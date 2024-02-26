from pydantic import BaseModel


class InterfaceConfig(BaseModel):
    name: str
    description: str
    ip_address: str
    subnet_mask: str
