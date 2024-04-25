import requests
import json
from string import Template



# Función get para traer la información desde la API:

def request_get(url):
    return json.loads(requests.get(url).text)

out = request_get("https://aves.ninjas.cl/api/birds")

#print(out[0]["images"]["main"]) # ubicación de la imagen del elemento 1/214



# Templates ("plantillas"):

img_template = Template("<img src='$url'>")

html_Template = Template('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aves de Chile</title>
</head>
<body>
    <h1>Aves de Chile</h1>
    
    $body
    
</body>
</html>''')


lista_url = []

for elemento in out:
    imagen_ave = elemento["images"]["main"]
    lista_url.append(imagen_ave)

texto_img = " "

for url_lista in lista_url:
    texto_img += img_template.substitute(url = url_lista)

print(texto_img)



html = html_Template.substitute(body = texto_img)

with open("index.html", "w") as f:
    f.write(html)