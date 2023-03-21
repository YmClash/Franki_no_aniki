import sqlite3
from sqlite3 import Error
import chatterbot
import logging
import conversation
import aniki_Lib
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

logging.basicConfig(level=logging.INFO)

aniki = chatterbot.ChatBot("Aniki")

teacher = ChatterBotCorpusTrainer(aniki)
teacher.train("chatterbot.corpus.french")

trainer = ListTrainer(aniki)

trainer.train(conversation.conversation_EN)
trainer.train(conversation.cconversation_FR)
trainer.train(conversation.conversations_suisse)
trainer.train(conversation.conversations_python)

while True :
    user_input = input(f'YMC: ')
    response = aniki.get_response(user_input)
    print(f'Aniki : {response}')

    if user_input.lower() == "exit" :
        print(f'Aniki: Aurevoir')
        break


ip = aniki_Lib.ip_adresse()


