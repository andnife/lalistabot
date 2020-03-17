from config import getApi
import random

# api twitter
api = getApi()
def postStatus(update):
    api.PostUpdate(update)

# crear listas
list1 = []
list2 = []

# abrir txt1 r, guardar frases en lista1, escoger frase, borrar frase de lista1, cerrar txt1
f=open('1.txt', 'r', encoding='latin1', errors = 'replace')
list1 = f.readlines()
a = random.randint(1, len(list1))
tweet = list1[a]
del list1[a]
f.close()

# abrir txt1 w, escribir lista1
f=open('1.txt', 'w', encoding='latin1', errors = 'replace')
f.writelines(list1)
f.close()

# abrir txt2 r, guardar frases en lista2, agregar frase, cerrar txt2
f=open('2.txt', 'r', encoding='latin1', errors = 'replace')
list2 = f.readlines()
list2.append(tweet)
f.close()

# abrir txt2 r, escribir lista2, cerrar txt2
f=open('2.txt', 'w', encoding='latin1', errors = 'replace')
f.writelines(list2)
f.close()

# postear tweet
postStatus(tweet)
