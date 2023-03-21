import discord
import requests
import socket


def ip_adresse() :
    hostname = socket.gethostname()
    ip_adresse = socket.gethostbyname(hostname)
    print(f'votre adresse IP est : {ip_adresse}')


def create_connection():

    database =None;
    try:
        database = sqlite3.connect(':memory')
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if database:
            database.close()

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
#
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
