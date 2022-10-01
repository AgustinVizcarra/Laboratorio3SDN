import yaml
with open("info.yaml", "r") as stream:
    try:
        data = yaml.safe_load(stream)
        servidores = data["servidores"]
        i=0
        for servidor in servidores:
            print("Servidor "+str(i+1)+": "+servidor["nombre"])
            i+=1
    except yaml.YAMLError as exc:
        print(exc)
