import discord
import requests
import socket
import logging
import webbrowser
import os
import sys
import sqlite3
import random
import secrets



logging.basicConfig(level=logging.INFO)

def ip_adresse() :
    hostname = socket.gethostname()
    ip_adresse = socket.gethostbyname(hostname)
    print(f'votre adresse IP est : {ip_adresse}')





def create_connection_database():

    database =None;
    try:
        database = sqlite3.connect(':memory')
        print(sqlite3.version)
    except EOFError as e:
        print(e)
    finally:
        if database:
            database.close()



def compare_list(liste1:list,liste2:list):
    resultat = set(liste1) & set(liste2)
    if len(resultat) > 0:
        print(f'il ya {len(resultat)} Element communs : {resultat}')
    else:
        print(" Il n'ya pas d'element en commun ")



numb_1 = [random.randint(1,10) for i in range(10)]
numb_2 = [random.randint(1,10) for e in range(10)]

compare_list(numb_1,numb_2)

# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
# #
# # Création du chatbot
# chatbot = ChatBot("MonChatbot")
#
# # Configuration de l'entraîneur
# entraineur = ChatterBotCorpusTrainer(chatbot)
#
# # Entraînement du chatbot avec le corpus de données en français
# entraineur.train("chatterbot.corpus.french")
#
#
# # Fonction pour obtenir une réponse du chatbot
# def obtenir_reponse(texte) :
#     reponse = chatbot.get_response(texte)
#     return reponse
#
#
# # Boucle pour discuter avec le chatbot
# while True :
#     texte_utilisateur = input("Vous: ")
#
#     if texte_utilisateur.lower() == "quitter" :
#         print("Chatbot: Au revoir !")
#         break
#
#     reponse_chatbot = obtenir_reponse(texte_utilisateur)
#     print("Chatbot:", reponse_chatbot)
#
#
#
# aniki = chatterbot.ChatBot('terminal', storage_adapter='chatterbot.storage.SQLStorageAdapter',
#                            logic_adapters=['chatterbot.logic.MathematicalEvaluation',
#                                            'chatterbot.logic.TimeLogicAdapter', 'chatterbot.logic.BestMatch'],
#                            database_uri='sqlite:///database.db')


ip_adresse()
