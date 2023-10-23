import json

json_data = """
{
  "router": [
      {
          "hostname": "Router1",
          "fabricante": "Cisco",
          "modelo": "ASR9K",
          "ip": "192.168.56.200"
      },
      {
          "hostname": "Router2",
          "fabricante": "Huawei",
          "modelo": "NE40E",
          "ip": "192.168.56.250"
      }
  ]

}
"""
# Convertir string JSON en diccioario
json_dict = json.loads(json_data)

# Imprimir el diccionario
print(json.dumps(json_dict, indent=4))

# Imprimir hostname e IP
for router in json_dict["router"]:
    print(f"Hostname: {router['hostname']}, IP: {router['ip']}")

# Insertar la información de nuevo equipo
router_nuevo = {
    "hostname": "Router3",
    "fabricante": "Cisco",
    "modelo": "CSR",
    "ip": "192.168.56.210",
}
json_dict["router"].append(router_nuevo)

# Cambiar la IP de Router2 a 192.168.56.111
for router in json_dict["router"]:
    if router["hostname"] == "Router2":
        router["ip"] = "192.168.56.111"

# Convertir el diccionario en una cadena XML
json_string = json.dumps(json_dict, indent=4)

# Imprimir la cadena json resultante
print(json_string)
