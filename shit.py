import discord
import subprocess
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv('MTI0NTAxMTgzNTgyOTM1NDU0Nw.G87-w3.7sQQfDH-AC0DUy4JaET_IFVAomBLExEs7LqjNQ')

# Set up the bot client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Commands should start with the '!' prefix
    if message.content.startswith('!'):
        command = message.content[1:]  # Remove '!' from the command
        
        if command.startswith('open '):
            file_to_open = command[len('open '):]
            try:
                if os.name == 'nt':
                    os.startfile(file_to_open)  # Windows-specific
                else:
                    subprocess.Popen(['xdg-open', file_to_open])  # Linux-specific
                await message.channel.send(f'Opened: {file_to_open}')
            except Exception as e:
                await message.channel.send(f'Failed to open file: {e}')

        elif command.startswith('close '):
            process_name = command[len('close '):]
            try:
                if os.name == 'nt':
                    subprocess.run(['taskkill', '/IM', process_name, '/F'])
                else:
                    subprocess.run(['pkill', process_name])
                await message.channel.send(f'Closed process: {process_name}')
            except Exception as e:
                await message.channel.send(f'Failed to close process: {e}')

        elif command == 'shutdown':
            try:
                if os.name == 'nt':
                    subprocess.run(['shutdown', '/s', '/t', '0'])
                else:
                    subprocess.run(['shutdown', 'now'])
                await message.channel.send('Shutting down...')
            except Exception as e:
                await message.channel.send(f'Failed to shut down: {e}')

# Run the bot
client.run(TOKEN)
