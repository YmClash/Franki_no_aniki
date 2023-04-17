from datasets import load_dataset
from transformers import GPT2Tokenizer

train_data = load_dataset("text", data_files={"train":"path/to/mytrain/data.txt "})















#
# conversation_EN = ([
#     "Hello",
#     "Hi there!",
#     "how are you doing?",
#     "i'm doing great.",
#     "That is good to hear",
#     "Thank you .",
#     "You're Welcome"
# ])
#
# cconversation_FR = [
#     "Salut !",
#     "Bonjour !",
#     "Comment ça va ?",
#     "Ça va bien, merci ! Et vous ?",
#     "Quel âge avez-vous ?",
#     "En tant que chatbot, je n'ai pas d'âge.",
#     "Quel est votre nom ?",
#     "Je suis Franki No Aniki, un chatbot Perso dev par Y_Mc.",
#     "Quelle est la météo aujourd'hui ?",
#     "Je suis désolé, je ne peux pas fournir d'informations en temps réel sur la météo.",
#     "Qui a créé OpenAI ?",
#     "OpenAI a été fondée par Elon Musk, Sam Altman, Greg Brockman, Ilya Sutskever, John Schulman et Wojciech Zaremba.",
#     "Pouvez-vous parler d'autres langues ?",
#     "Oui, je peux communiquer dans plusieurs langues, dont l'anglais, le français, l'espagnol, l'allemand et bien "
#     "d'autres.",
#     "Qu'est-ce que l'intelligence artificielle ?",
#     "L'intelligence artificielle (IA) est un domaine de recherche en informatique qui vise à créer des machines "
#     "capables d'accomplir des tâches normalement réservées aux humains, comme la reconnaissance de la parole, "
#     "la compréhension du langage naturel, l'apprentissage et la résolution de problèmes.",
#     "Qu'est-ce que le machine learning ?",
#     "Le machine learning, ou apprentissage automatique, est une sous-branche de l'intelligence artificielle qui se concentre sur le développement d'algorithmes et de modèles permettant aux machines d'apprendre et de s'améliorer avec le temps en s'appuyant sur des données et des expériences.",
# ]
#
# conversations_suisse = [
#     "Quelle est la capitale de la Suisse ?",
#     "La capitale de la Suisse est Berne.",
#     "Combien de langues officielles la Suisse a-t-elle ?",
#     "La Suisse a quatre langues officielles : l'allemand, le français, l'italien et le romanche.",
#     "Quelle est la monnaie utilisée en Suisse ?",
#     "La monnaie utilisée en Suisse est le franc suisse (CHF).",
#     "Quels sont les pays voisins de la Suisse ?",
#     "La Suisse est entourée de cinq pays : la France, l'Allemagne, l'Italie, l'Autriche et le Liechtenstein.",
#     "Quel est le système politique de la Suisse ?",
#     "La Suisse est une démocratie semi-directe et une république fédérale.",
#     "Quel est le drapeau de la Suisse ?",
#     "Le drapeau suisse est composé d'un fond rouge avec une croix blanche au centre.",
#     "Quelle est la plus grande ville de Suisse ?",
#     "La plus grande ville de Suisse est Zurich.",
#     "Quel est le nom officiel de la Suisse ?",
#     "Le nom officiel de la Suisse est la Confédération suisse.",
#     "Quelle est la population de la Suisse ?",
#     "La population de la Suisse est d'environ 8,5 millions de personnes (en 2021).",
#     "Quelle est la superficie de la Suisse ?",
#     "La superficie de la Suisse est d'environ 41 290 kilomètres carrés.",
# ]
#
# conversations_python = [
#     "Qu'est-ce que Python ?",
#     "Python est un langage de programmation à haut niveau, orienté objet, interprété et facile à apprendre. Il a été "
#     "créé par Guido van Rossum et est largement utilisé pour le développement web, l'analyse de données, "
#     "l'intelligence artificielle et d'autres applications.",
#     "Qui a créé Python ?",
#     "Python a été créé par Guido van Rossum en 1989.",
#     "Comment installer Python ?",
#     "Pour installer Python, rendez-vous sur le site officiel (python.org) et téléchargez l'installateur correspondant "
#     "à votre système d'exploitation. Suivez ensuite les instructions pour l'installation.",
#     "Qu'est-ce qu'une variable en Python ?",
#     "Une variable en Python est un conteneur pour stocker des données. Les variables peuvent contenir des valeurs "
#     "numériques, des chaînes de caractères, des listes, des dictionnaires et d'autres types de données.",
#     "Comment déclarer une variable en Python ?",
#     "En Python, vous pouvez déclarer une variable en attribuant une valeur à un nom. Par exemple : `ma_variable = 42`.",
#     "Qu'est-ce qu'une liste en Python ?",
#     "Une liste en Python est une collection ordonnée et modifiable d'éléments. Les listes sont déclarées entre "
#     "crochets, avec les éléments séparés par des virgules. Par exemple : `ma_liste = [1, 2, 3, 4, 5]`.",
#     "Comment ajouter un élément à une liste en Python ?",
#     "Pour ajouter un élément à une liste en Python, utilisez la méthode `append()`. Par exemple : `ma_liste.append(6)`.",
#     "Qu'est-ce qu'un tuple en Python ?",
#     "Un tuple en Python est une collection ordonnée et non modifiable d'éléments. Les tuples sont déclarés entre "
#     "parenthèses, avec les éléments séparés par des virgules. Par exemple : `mon_tuple = (1, 2, 3, 4, 5)`.",
#     "Qu'est-ce qu'un dictionnaire en Python ?",
#     "Un dictionnaire en Python est une collection non ordonnée de paires clé-valeur. Les dictionnaires sont déclarés "
#     "entre accolades, avec les paires clé-valeur séparées par des virgules. Par exemple : `mon_dictionnaire = {"
#     "'clé1': 'valeur1', 'clé2': 'valeur2'}`.",
#     "Comment écrire une fonction en Python ?",
#     "En Python, une fonction est définie à l'aide du mot-clé `def`, suivi du nom de la fonction, de parenthèses et "
#     "d'un deux-points. Le code de la fonction doit être indenté. Par exemple :\n\ndef ma_fonction():\n    print("
#     "'Bonjour !')",
#     "Comment écrire une boucle `for` en Python ?",
#     "En Python, une boucle `for` est utilisée pour parcourir les éléments d'une collection, comme une liste ou un "
#     "tuple. Voici un exemple :\n\nfor i in range(5):\n    print(i)",
#     "Comment écrire une boucle `while` en Python ?",
#
# ]