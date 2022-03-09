import xml.etree.ElementTree as ET
from xml.dom import minidom

ruta= "E:/Archivos del pc/Descargas/xml/xml y lector en python/xml diferente/"

xml = minidom.parse(ruta+"DispositivosElectronicos.xml")

archivo_xml = ET.parse(ruta+"DispositivosElectronicos.xml")
raiz = archivo_xml.getroot()

print(raiz)
docs = xml.getElementsByTagName("DispositivosElectronicos")

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
                
#for DispositivosElectronicos in docs: 
 #   nodo1 = DispositivosElectronicos.getElementsByTagName("Computador")[0]
  #  nodo2 = DispositivosElectronicos.getElementsByTagName("Celular")[0]
   # nodo3 = DispositivosElectronicos.getElemtsByTagName("Impresora")[0]
    #print(f"nodo1={nodo1.firstChild.data}")
    #print(f"nodo2={nodo2.firstChild.data}")
    #print(f"nodo3={nodo3.firstChild.data]")
