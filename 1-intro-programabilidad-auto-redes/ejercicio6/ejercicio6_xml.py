import xmltodict
import json

xml_data = """
<routers>
  <router>
    <hostname>Router1</hostname>
    <fabricante>Cisco</fabricante>
    <modelo>ASR9K</modelo>
    <ip>192.168.56.200</ip>
  </router>
  <router>
    <hostname>Router2</hostname>
    <fabricante>Huawei</fabricante>
    <modelo>NE40E</modelo>
    <ip>192.168.56.250</ip>
  </router>
</routers>
"""
xml_ordered_dict = xmltodict.parse(xml_data)

# Convertir de un Diccionario Ordenado a un Diccionario estandar
xml_dict = dict(xml_ordered_dict)

# Imprimir el diccionario
print(json.dumps(xml_dict, indent=4))

# Imprimir hostname e IP
for router in xml_dict["routers"]["router"]:
    print(f"Hostname: {router['hostname']}, IP: {router['ip']}")
