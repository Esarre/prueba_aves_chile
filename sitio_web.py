import requests
import json
from string import Template



# Función get para traer la información desde la API:

def request_get(url):
    return json.loads(requests.get(url).text)

out = request_get("https://aves.ninjas.cl/api/birds")

#print(out[0]["images"]["main"]) # ubicación de la imagen del elemento 1/214



# Templates ("plantillas"):

img_template = Template("<div class='row mx-auto col-3'><img src='$url'><h5 class='text-white'>Nombre:</h5><p class='text-white'>Espanol: '$name_sp'</p><p class='text-white'>Ingles: '$name_en'</p></div>")

body_content = " "

for ave in out:
    imagen_url = ave["images"]["main"]
    nombre_sp = ave["name"]["spanish"]
    nombre_en = ave["name"]["english"]

    body_content += img_template.substitute(url=imagen_url, name_sp=nombre_sp, name_en=nombre_en)



html_Template = Template('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aves de Chile</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css">
</head>
<body class="bg-dark">
    <h1 class="text-center text-white mb-5">Aves de Chile</h1>
<section class="container row mx-auto">
    $body
</section>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>''')



html = html_Template.substitute(body = body_content)
print(html)

with open("index.html", "w") as f:
    f.write(html)