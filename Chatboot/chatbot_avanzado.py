# Para instalar
# $ pip install --user -U nltk

from nltk import word_tokenize, Text, FreqDist
from nltk.chat.util import Chat, reflections
import re
import random

class MyChat(Chat):
    etiquetas = {}

    def __init__(self, pairs, reflections={}):

        # add `z` because now items in pairs have three elements
        self._pairs = [(re.compile(x, re.IGNORECASE), y, z) for (x, y, z) in pairs]
        self._reflections = reflections
        self._regex = self._compile_reflections()


    def respond(self, str):

        """
        Redefinimos el método que genera la respuesta.
        El objetivo es poder hacer el análisis de palabras.

        :type str: str
        :param str: Cadena a ser mapeada para dar respuesta
        :rtype: str
        """

        flag_match = True
        if(flag_match):
            # desarma una cadena en tokens (palabras o  etiquetas) y uso un diccionario para
            # contar ocurrencias.
            tokens = word_tokenize(str)
            for tok in tokens:
                if tok not in self.etiquetas:
                    self.etiquetas[tok] = 1
                else:
                    self.etiquetas[tok] += 1

            flag_match = False

        # Bucle que verifica si el parámetro hace match con alguna de las reglas.
        # En base a esto elabora la respuesta y llama a una función si aplica.

        for (pattern, response, callback) in self._pairs:
            match = pattern.match(str)

            if match:

                resp = random.choice(response)
                resp = self._wildcards(resp, match)

                if resp[-2:] == '?.':
                    resp = resp[:-2] + '.'
                if resp[-2:] == '??':
                    resp = resp[:-2] + '?'

                # run `callback` if exists
                if callback: # eventually: if callable(callback):
                    callback(match)

                return resp



def reg_hosting(match):
    print("Pregunta por el hosting")

def resumen(match):
    print(MyChat.etiquetas)



mis_reflexions = {
"ir": "fui",
"hola": "hey"
}

pares = [
    [
        r"(.*)caido(.*)hosting(.*)",
        ["Sentimos ese fallo, para reiniciarlo, entra en CPANEL y selecciona reiniciar"],
        reg_hosting
    ],
    [
        r"(.*)(email|telefono|direccion)",
        ["Nuestros datos de contacto son: XX YY ZZ", ],
        None
    ],
    [
        r"(.*)no anda(.*)hosting(.*)",
        ["Sentimos ese fallo, para reiniciarlo, entra en CPANEL y selecciona reiniciar", ],
        None
    ],
    [
        r"resumen",
        ["Este fué el resumen de tus búsquedas.", ],
        resumen
    ],
    [
        r"mi nombre es|soy (.*)",
        ["Hola %1, en que puedo ayudarte ?", ],
        None
    ],
     [
        r"(.*)pagar(.*)factura(.*)",
        ["Hay que pagarla el dia 15 de cada mes por tarjeta de crédito", ],
        None
    ],
    [
        r"(.*) ampliar el servicio",
        ["Para ampliar el servicio, contacta con facturacion",],
        None
    ],
    [
        r"disculpa (.*)",
        ["No pasa nada",],
        None
    ],
    [
        r"hola|hey|buenas",
        ["Hola", "Que tal",],
        None
    ],
    [
        r"que (.*) quieres ?",
        ["Nada gracias",],
        None
    ],
    [
        r"(.*) creado ?",
        ["Fui creado hoy",],
        None
    ],
    [
        r"finalizar",
        ["Chao","Fue bueno hablar contigo"],
        None
    ],
]
def chatear():
    print("Hola, soy el servicio de hosting") #mensaje por defecto
    chat = MyChat(pares, mis_reflexions)
    chat.converse()

if __name__ == "__main__":
    chatear()

chatear()