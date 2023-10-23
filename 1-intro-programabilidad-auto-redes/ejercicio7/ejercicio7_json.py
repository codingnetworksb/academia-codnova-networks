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
