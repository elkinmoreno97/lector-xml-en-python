import xml.etree.ElementTree as ET

ruta= "E:/Archivos del pc/Descargas/xml/xml y lector en python/"

archivo_xml = ET.parse(ruta+"DispositivosElectronicos.xml")

raiz = archivo_xml.getroot()

print(raiz)
print(raiz.text)

for hijo in raiz:
    print(hijo)
    print(hijo.text)

    for hijo2 in hijo:
        print(hijo2)
        print(hijo2.text)

        for hijo3 in hijo2:
            print(hijo3)
            print(hijo3.text)

            for hijo4 in hijo3:
                print(hijo4)
                print(hijo4.text)