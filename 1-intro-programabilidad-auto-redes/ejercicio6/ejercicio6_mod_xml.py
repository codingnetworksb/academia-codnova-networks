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


# Insertar la información de nuevo equipo
router_nuevo = {
    "hostname": "Router3",
    "fabricante": "Cisco",
    "modelo": "CSR",
    "ip": "192.168.56.210",
}
xml_dict["routers"]["router"].append(router_nuevo)

# Cambiar la IP de Router2 a 192.168.56.111
for router in xml_dict["routers"]["router"]:
    if router["hostname"] == "Router2":
        router["ip"] = "192.168.56.111"

# Convertir el diccionario en una cadena XML
xml_string = xmltodict.unparse(xml_dict, pretty=True)

# Imprimir la cadena XML resultante
print(xml_string)
