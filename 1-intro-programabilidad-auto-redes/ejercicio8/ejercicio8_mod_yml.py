import yaml
import json

yaml_data = """
---
router:
  - hostname: Router1
    fabricante: Cisco
    modelo: ASR9K
    ip: 192.168.56.200
  - hostname: Router2
    fabricante: Huawei
    modelo: NE40E
    ip: 192.168.56.250
"""
yaml_dict = yaml.load(yaml_data, Loader=yaml.FullLoader)

# Imprimir el diccionario
print(json.dumps(yaml_dict, indent=4))

# Imprimir hostname e IP
for router in yaml_dict["router"]:
    print(f"Hostname: {router['hostname']}, IP: {router['ip']}")

# Insertar la información de nuevo equipo
router_nuevo = {
    "hostname": "Router3",
    "fabricante": "Cisco",
    "modelo": "CSR",
    "ip": "192.168.56.210",
}
yaml_dict["router"].append(router_nuevo)

# Cambiar la IP de Router2 a 192.168.56.111
for router in yaml_dict["router"]:
    if router["hostname"] == "Router2":
        router["ip"] = "192.168.56.111"

# Convertir el diccionario en una cadena XML
json_string = yaml.dump(yaml_dict)

# Imprimir la cadena json resultante
print(json_string)
