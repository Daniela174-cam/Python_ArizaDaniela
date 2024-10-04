import json

data =  {}
data ["jugadores"]=[]
data["jugadores"].append({
     "nombre": "daniela",
     "apellido":"ariza", 
     "apodo":"dani"
})
data["jugadores"].append({
    "nombre":"sara",
    "apellido":"bandera",
    "apodo":"saris"
})
with open('data.json', 'w')as file:
    json.dump(data, file, indent=4)
    