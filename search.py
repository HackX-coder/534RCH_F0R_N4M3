import requests
from bs4 import BeautifulSoup
import urllib.parse
import time
import sys

def imprimir_en_tiempo_real(texto, velocidad=0.02):
    for caracter in texto:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(velocidad)

def buscar_en_internet(nombre, apellidos):
    consulta = f"{nombre} Instagram OR '{nombre}' OR '{apellidos}'"

    for pagina in range(0, 30, 10):
        url = f"https://www.google.com/search?q={urllib.parse.quote(consulta)}&start={pagina}"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            resultados = soup.find_all('div', class_='g')

            for resultado in resultados:
                titulo = resultado.find('h3')
                enlace = resultado.find('a')['href'] if resultado.find('a') else None

                if titulo and enlace:
                    imprimir_en_tiempo_real(f'Titulo: {titulo.get_text()}\n')
                    imprimir_en_tiempo_real(f'Enlace: {enlace}\n\n')

        else:
            imprimir_en_tiempo_real(f'Error: {response.status_code}\n')

        time.sleep(3)

if __name__ == "__main__":
    nombre = input("Enter Name: ")
    apellidos = input("Enter Last Name: ")
    buscar_en_internet(nombre, apellidos)
