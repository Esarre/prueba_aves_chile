import requests
import json
from string import Template



# Función get para traer la información desde la API:

def request_get(url):
    return json.loads(requests.get(url).text)

out = request_get("https://aves.ninjas.cl/api/birds")

#print(out[0]["images"]["main"]) # ubicación de la imagen del elemento 1/214



# Templates ("plantillas"):

    # Plantilla para el contenido (imagen, nombre en español, nombre en inglés):

img_template = Template("<div class='row mx-auto col-3'>\n<img src='$url'><h5 class='text-white'>Nombre:</h5>\n<p class='text-white'>Espanol: '$name_sp'</p>\n<p class='text-white'>Ingles: '$name_en'</p>\n</div>")


    # Comienzo de la iteración del contenido (un string vacío):

body_content = " "

    # Iteración que permite obtener la información en el orden imagen - nombre en español - nombre en inglés. Por cada iteraciíon, el contenido se irá almacenando en la variable "body_content":
for ave in out:
    imagen_url = ave["images"]["main"]
    nombre_sp = ave["name"]["spanish"]
    nombre_en = ave["name"]["english"]

    body_content += img_template.substitute(url=imagen_url, name_sp=nombre_sp, name_en=nombre_en)


    # Plantilla con el formato para crear el archivo html:

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


# Sustitución de la "variable" definida en el html como "$body", por el contenido que nos interesa (imágenes, nombre en español y nombre en inglés), el que se encuentra en la variable "body_content":

html = html_Template.substitute(body = body_content)
print(html)
# Todo el contenido, entonces, se almacena en la variable "html", y se procede a imprimir por consola con el "print(html)" para aplicar los cambios.



# Con el siguiente código, se procede a definir que cuando se corra el programa, se cree ("escriba") un archivo "index.html" que tenga el formato html que almacena la variable con el nombre "html":

with open("index.html", "w") as f:
    f.write(html)

# Entonces, si queremos realizar algún cambio al código, para que estos cambios los podamos ver en el navegador debemos correr el programa para que se genere un nuevo archivo "index.html" (que en realidad no se genera uno nuevo, sino que al existir un archivo "index.html" generado con anterioridad solo se sobreescribe; ahora, si borramos el archivo "index.html" y corremos el programa, en este caso se creará un nuevo archivo).