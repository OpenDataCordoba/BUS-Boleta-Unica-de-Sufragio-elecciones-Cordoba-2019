import requests
import json
import os

lista_json = 'lista.json'

def download_lista():
    print('Decargando')
    req = requests.get('https://www.justiciacordoba.gob.ar/Estatico/JEL/Contenido/BusVisor/busvisor.json')
    text = req.text
    f = open(lista_json, 'w')
    f.write(text)
    f.close()
    return text

if not os.path.exists(lista_json):
    text = download_lista()
else:
    print('Leyendo')
    f = open(lista_json, 'r')
    text = f.read()
    f.close()

lista = json.loads(text)

data = lista['data'][1]['data'][0]

for dt in data:
    d = data[dt]
    url = 'https://www.justiciacordoba.gob.ar{}'.format(d['fileName'])
    
    req = requests.get(url)
    fname = 'BUSes/{}.pdf'. format(d['Descripcion'])
    fname = fname.encode('iso-8859-1')

    print('Descargando {}'.format(fname))
    f = open(fname, 'wb')
    f.write(req.content)
    f.close()

    for loc in d['localidades']:
        d = loc
        url = 'https://www.justiciacordoba.gob.ar{}'.format(d['fileName'])
        req = requests.get(url)
        fname = 'BUSes/{}.pdf'. format(d['Descripcion'])
        fname = fname.encode('iso-8859-1')
        print('Descargando {}'.format(fname))
        f = open(fname, 'wb')
        f.write(req.content)
        f.close()


