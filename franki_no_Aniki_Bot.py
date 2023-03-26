import random
import openai
import lorem
import openai
import discord
import responses
import quotes
import os
from dotenv import load_dotenv

# This example requires the 'message_content' intent.


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

load_dotenv()

clee = os.getenv('DISCORD_API_KEY')
if not clee:
    raise ValueError('DISCORD API KEY is not difined in the .env file ')




quotes = quotes.quotes


# quotes = ["C'est dans le besoin qu'on reconnaît ses vrais amis.",
#          "Il n'est pire aveugle que celui qui ne veut pas voir. Il n'est pire sourd que celui qui ne veut pas entendre.",
#          "Les yeux ont toujours faim de voir.",
#          "La patience est amère, mais son fruit est doux.",
#          "A vouloir trop avoir, l'on perd tout.",
#          "Quand la pauvreté entre par la porte, l'amour s'en va par la fenêtre.",
#          "Donne ton amour à ta femme et donne ton secret à ta mère.",
#          "Sagesse, beauté et gentillesse ne font bouillir aucun chaudron.",
#          "Le mal retourne à celui qui le fait.",
#          "Qui se nourrit d'attente risque de mourir de faim."]


def run_aniki() :
    TOKEN = clee


@client.event
async def on_ready() :
    print(f'We have logged in as {client.user}')


@client.event
async def on_message(message) :
    if message.author == client.user :
        return

    if message.content.startswith('hello') :
        await message.channel.send('Hello!')

    if message.content.startswith('cava') :
        await message.channel.send('je vais bien  et vous ')

    if message.content.startswith('roll 1') :
        roll = random.randint(1, 6)
        await message.channel.send(str(roll))

    if message.content.startswith("roll 2") :
        roll = ([random.randint(0, 10) for i in range(2)])
        await message.channel.send(str(roll))

    if message.content.startswith("roll 3") :
        roll = ([random.randint(0, 10) for i in range(3)])
        await message.channel.send(str(roll))

    if message.content.startswith("roll 4") :
        roll = ([random.randint(0, 10) for i in range(4)])
        await message.channel.send(str(roll))

    if message.content.startswith("roll 10") :
        roll = ([random.randint(0, 10) for i in range(10)])
        await message.channel.send(str(roll))

    if message.content.startswith("text") :
        text = lorem.sentence()
        await message.channel.send(str(text))

    if message.content.startswith("quote") :
        quote = random.choice(quotes)
        await message.channel.send(str(quote))


client.run(clee)







"""
async def send_message(message, user_message, is_private) :
    try :
        response = responses.handle_response(user_message)
        await  message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e :
        print(e)


def run_discord_bot() :
    TOKEN = 'MTA3ODQ0NTAyMDU1MTU4OTg4OA.GK8QEb.AI3rRcQ6FxSgaa8t8VhXfnN3evuWhrhb0i5twU'

    @client.event()
    async def on_ready() :
        print(f"{client.user} is now running")

    @client.event()
    async def on_message(message) :
        if message.author == client.user :
            return

        username = str(message.author)
        user_message = str(message.content)
        channel == str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] == '?' :
            user_message = user_message[1 :]
            await send_message(message, user_message, is_private=True)
        else :
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)
"""
