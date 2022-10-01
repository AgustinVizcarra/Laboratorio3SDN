import requests
#Inciso 1
#Fuente : https://floodlight.atlassian.net/wiki/spaces/floodlightcontroller/pages/1343621/DeviceManagerImpl+Dev
#Inciso 2
def get_attachment_points(mac):
    api = "http://10.20.12.64:8080/wm/device/"
    response = requests.get(api, params={"mac":mac})
    data = response.json()[0]
    relevantInfo = data["attachmentPoint"][0]
    switchDPID = relevantInfo["switchDPID"]
    outputPort = relevantInfo["port"]
    return[switchDPID, outputPort]
#Inciso 3
#Considerando el apartado de APIS de Topology y Routing
def getRoute(DPID_src,port_source,DPID_dest,port_dest):
    api = "http://10.20.12.64:8080/wm/topology/route/"
    api = api + "/" + DPID_src + "/" + str(port_source) + "/" + DPID_dest + "/" + str(port_dest) + "/json" 
    response  = requests.get(api)
    data = response.json()
    print("Ruta del Switch con DPID: "+DPID_src+" hacia el Switch con DPID: "+DPID_dest)
    print("----------------------------------------------------------------")
    counter = 0
    for hop in data:
        print(str(counter+1)+". DPID: "+hop["switch"]+" por el puerto: "+str(hop["port"]["portNumber"]))
        counter += 1
    print("----------------------------------------------------------------")        
if __name__ == "__main__":
    #Esta direccion corresponde a la direccion del Host 1
    mac_h1 = "fa:16:3e:52:5c:3b"
    mac_h2 = "fa:16:3e:02:79:e5"
    parameters_h1 = get_attachment_points(mac_h1)
    parameters_h2 = get_attachment_points(mac_h2)
    print("Parametros Host 1("+mac_h1+"): "+str(parameters_h1))
    print("Parametros Host 2("+mac_h2+"): "+str(parameters_h2))
    #Considerando los parametros de conexión del host 1 y host 2 se hallará la ruta
    getRoute(parameters_h1[0],parameters_h1[1],parameters_h2[0],parameters_h2[1])
