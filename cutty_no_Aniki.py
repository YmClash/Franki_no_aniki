import huggingface_hub
import discord
import os
import torch
import aniki_Lib
from transformers import  GPT2Tokenizer ,GPT2LMHeadModel


from dotenv import load_dotenv


load_dotenv()

huggingkey = os.getenv('FRANKI_NO_ANIKI')




model_name = "distilgpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def get_response():
    # Tokenize et générer la réponse
    prompt=input("YMC: ")
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    attention_mask = input_ids.ne(tokenizer.pad_token_id).long()


    output = model.generate(input_ids, max_length=50, num_return_sequences=1,
                            attention_mask=attention_mask,
                            pad_token_id=tokenizer.eos_token_id)

    # Décoder la réponse
    response = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)

    print(response)




get_response()



#
#
# tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
# model = GPT2Model.from_pretrained('gpt2')t_response(bonjour)
#
# while True:
#     user_input = input("YMC: ")
#     text = user_input
#     encoded_input = tokenizer(text,return_tensors='pt')
#     decode
#     output = model(**encoded_input)
#     print(output)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
















# import sqlite3
# from sqlite3 import Error
# import chatterbot
# import logging
# import conversation
# import aniki_Lib
# from chatterbot.trainers import ListTrainer
# from chatterbot.trainers import ChatterBotCorpusTrainer
#
# logging.basicConfig(level=logging.INFO)
#
# aniki = chatterbot.ChatBot("Aniki")
#
# teacher = ChatterBotCorpusTrainer(aniki)
# teacher.train("chatterbot.corpus.french")
#
# trainer = ListTrainer(aniki)
#
# trainer.train(conversation.conversation_EN)
# trainer.train(conversation.cconversation_FR)
# trainer.train(conversation.conversations_suisse)
# trainer.train(conversation.conversations_python)
#
# while True :
#     user_input = input(f'YMC: ')
#     response = aniki.get_response(user_input)
#     print(f'Aniki : {response}')
#
#     if user_input.lower() == "exit" :
#         print(f'Aniki: Aurevoir')
#         break
#
#
ip = aniki_Lib.ip_adresse()


