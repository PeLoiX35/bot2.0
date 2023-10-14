import discord
from credits import token

t = token
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('!hello'):
        await message.channel.send(f'Привет!')
    if message.content.startswith('!list'):
        await message.channel.send(f'Пластик - 200-700 лет
                                    Стекло - 1000 лет
                                    Полиэтилен - 5-15 лет(в зависимости от плотности)
                                    Окурки - 2 года
                                    Железо - 10 лет
                                    Алюминий - 500 лет
                                    Бумага - 2 года
                                    Картон - 2 месяца
                                    Обьедки - 1 год
                                    Кирпичи - 10 лет
                                    оптоволокно - 600 лет')
    elif  message.content.startswith('!heh'):
        if len(message.content) > 4:
            count_heh = int(message.content[4:])
        else:
            count_heh = 5
        await message.channel.send("he" * count_heh)
        
client.run(t)