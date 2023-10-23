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
