#Crea un programa que se encargue de calcular el aspect ratio de una # type: ignore
# * imagen a partir de una url.
# * - Url de ejemplo:
# *   https://raw.githubusercontent.com/mouredevmouredev/master/mouredev_github_profile.png
# * - Por ratio hacemos referencia por ejemplo a los "16:9" de una
# *   imagen de 1920*1080px.

import requests
from io import BytesIO
from PIL import Image
from math import gcd


def calcular_aspect_ratio(ancho, alto):
    factor = gcd(ancho, alto)
    return f"{ancho // factor}:{alto // factor}"


url = "https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png"


response = requests.get(url)


if response.status_code == 200:
  
    imagen = Image.open(BytesIO(response.content))
    
  
    ancho, alto = imagen.size
    print(f"Dimensiones de la imagen -> Ancho: {ancho}, Alto: {alto}")
    
   
    ratio = calcular_aspect_ratio(ancho, alto)
    print(f"El aspect ratio de la imagen es: {ratio}")
else:
    print("Error al descargar la imagen")

