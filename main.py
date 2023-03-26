import discord
import responses
import franki_no_Aniki_Bot as bot
import cutty_no_Aniki
import quotes
import os
from dotenv import load_dotenv


load_dotenv()

clee = os.getenv('DISCORD_API_KEY')

if __name__ == '__main__':
    bot.client.run()
    cutty_no_Aniki.create_connection()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
