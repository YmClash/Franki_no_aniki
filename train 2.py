import secrets
import random
import lorem
import requests
import socket
import sqlite3
from sqlite3 import Error






numb = [secrets.randbelow(100) for i in range(10)]
number = [random.randint(0, 100) for e in range(10)]
text = [lorem.sentence()]
mots = []

quote = ["C'est dans le besoin qu'on reconnaît ses vrais amis.",
         "Il n'est pire aveugle que celui qui ne veut pas voir. Il n'est pire sourd que celui qui ne veut pas entendre.",
         "Les yeux ont toujours faim de voir.",
         "La patience est amère, mais son fruit est doux.",
         "A vouloir trop avoir, l'on perd tout.",
         "Quand la pauvreté entre par la porte, l'amour s'en va par la fenêtre.",
         "Donne ton amour à ta femme et donne ton secret à ta mère.",
         "Sagesse, beauté et gentillesse ne font bouillir aucun chaudron.",
         "Le mal retourne à celui qui le fait.",
         "Qui se nourrit d'attente risque de mourir de faim."]

print(f'Numb : {numb}  Longeur : {len(numb)}')
print(f'Number: {number}', f'Longeur : {len(number)}')

for i in iter(numb) :
    mots.append(i)

print(f'iteration 1')

print(f'Mots : {mots} la Longeur : {len(mots)}')

for e in enumerate(quote) :
    print(e)
    mots.append(e)

print(f'iteration 2')


provere = random.choice(quote)
print()
print(f'Random::{provere}')

url = requests.get(h)