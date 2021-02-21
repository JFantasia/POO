# Para instalar
# $ pip install --user -U nltk

from nltk.chat.util import Chat, reflections

# Se aplican expresiones regulares para determinar lo que ingresa el/la usuario/a
# (.*) representa cualquier cadena luego o antes de una palabra o frase.
# Por ejemplo mi nombre es (.*) hace match con "mi nombre es Sam", "mi nombe es Mariano Moreno",
# "mi nombre es Lucia pero me dice Lu"
# Luego en la respuesta, la referencia a %1 indica la expresión que tenga (.*),
# por ejemplo la respuesta a "mi nombre es Sam" sería "Hola Sam, como estas ?"

pares = [
    [
        r"mi nombre es (.*) apellido (.*)",
        ["Hola %1 %2, como estas ?" ,]
    ],
    [
        r"hola|Hola|Buen día|Buenas tardes|Qué tal",
        ["Hola, como estas ?", ]
    ],
    [
        r"cual es tu nombre ?",
        ["Mi nombre es Chatbot ?" ,]
    ],
    [
        r"como estas ?",
        ["Bien, y tu?" ,]
    ],
    [
        r"disculpa (.*)",
        ["No pasa nada" ,]
    ],
    [
        r"que (.*) quieres ?",
        ["Nada gracias" ,]

    ],
    [
        r"(.*)| creado (.*)|",
        ["Fui creado hoy" ,]
    ],
    [
        r"finalizar",
        ["Chao" ,"Fue bueno hablar contigo"]
    ],
]

mis_reflexions = {
"ir": "fui",
"hola": "hey"
}

def chatear():
    print("Hola soy un bot, escribe algo para comenzar")  # mensaje por defecto
    chat = Chat(pares, mis_reflexions)
    chat.converse()

# Indica que el incio del programa llama a la función chatear
if __name__ == "__main__":
    chatear()
