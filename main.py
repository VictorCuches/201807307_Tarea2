import json
import csv
from xml.dom import minidom

print("BIENVENIDO")
print("1. json")
print("2. csv")
print("3. xml")
b = int(input("Seleccione que tipo de archivo desea cargar: "))

def cargar_json(ruta):
    with open(ruta) as contenido:
        archivi = json.load(contenido)
        for element in archivi:
            print(element)

if b==1:
    print("-----------------------")
    print("-----Archivo .json-----")
    print("-----------------------")
    ruta = 'Tarea2/Practica1.json'
    cargar_json(ruta)
elif b==2:
    print("----------------------")
    print("-----Archivo .csv-----")
    print("----------------------")
    with open('Tarea2/archivo.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print("Apellido: {0}, Nombre1: {1}, Nombre2: {2}, Ciudad: {3}".format(row[0], row[1], row[2], row[3]))

elif b==3:
    print("----------------------")
    print("-----Archivo .xml-----")
    print("----------------------")
    doc_xml = minidom.parse("Tarea2/file.xml")
    hijos = doc_xml.getElementsByTagName("tag_hijo")
    
    for chid in hijos:
        
        nombre = chid.getElementsByTagName("nombre")[0]
        apellido = chid.getElementsByTagName("apellido")[0] 
        edad = chid.getElementsByTagName("edad")[0]
        pais = chid.getElementsByTagName("pais")[0]

        print("nombre: %s" % nombre.firstChild.data)
        print("apellido: %s" % apellido.firstChild.data)
        print("edad: %s" % edad.firstChild.data)
        print("pais: %s" % pais.firstChild.data)
        print(" ")
else:
    print("Opcion incorrecta, chau")