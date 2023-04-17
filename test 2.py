import webbrowser
import ccxt
import secrets
import random
import logging
import asyncio
import torch



cuda=torch.cuda.is_available()

print(cuda)


#
# async def principale():
#     task  = asyncio.create_task(secondaire())
#     print("A")
#     await asyncio.sleep(1)
#     print("B")
#     await task
#
#
# async def secondaire():
#     print("1")
#     await asyncio.sleep(2)
#     print("2")
#
#
# asyncio.run(principale())
#
#


#
# adresse_valide = ['reddit',
#                   'stackoverflow.com',
#                   'stackexchange.com']
#
# url = "https://www.google.ch/search?q="
#
# chrome_path = 'open -a /Applications/Google\ chrome.app'
# webbrowser.get(chrome_path).open(url)
#
