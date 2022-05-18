# бот для напоминаний в дискорде
# должна быть библиотека discord и python 3.8+
# -*- coding: utf-8 -*-

import discord
import time
import datetime

TOKEN="Your token here"

gif_links = ['https://media2.giphy.com/media/assg5OOFJZdBdKuB9v/giphy.gif?cid=ecf05e47ec8681cf202fcf64f66ec5f159cdc110129c0969&rid=giphy.gif&ct=g', 'https://media2.giphy.com/media/assg5OOFJZdBdKuB9v/giphy.gif?cid=ecf05e47ec8681cf202fcf64f66ec5f159cdc110129c0969&rid=giphy.gif&ct=g', 'https://media1.giphy.com/media/s5FrAdw92uMq0UIC76/giphy.gif?cid=790b761196ca1c04e6690010e5fd321cab929dfba76991d4&rid=giphy.gif&ct=g']

chanels_id = [976459264094785579, 976464179961671740, 976464551065296936]

# список id чатов

times_list = [datetime.datetime(2000, 1, 1, 22, 2, 0), datetime.datetime(2000, 1, 1, 22, 12, 0), datetime.datetime(2000, 1, 1, 22, 22, 0)]
# время для каждого напоминания в формате (год, мес, день, час, минута, секунда)
# год, месяц и день НЕ МЕНЯТЬ, бот настроен на ежедневные уведомления

messages = ['@everyone Событие начнется через час.', '@everyone Событие началось.', '@everyone, до конца события 10 минут.']
#сообщения для чатов

activated = False
# определяет статус бота

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$start'):
        if activated==False :
            #сообщаем, что бот включился
            await message.channel.send('Started!')

            while True:
                now = datetime.datetime.now()

                j = 0
                while j < 3:
                    if times_list[j].hour == now.hour and times_list[j].minute == now.minute:
                        print('напоминаем ' + str(j))
                        message.channel.id = chanels_id[j]
                        await message.channel.send(messages[j])
                        time.sleep(3)
                        await message.channel.send(gif_links[j])
                        time.sleep(60)
                    j += 1

                time.sleep(0.5)

        else:
            #если бот уже запущен, сообщаем пользователю
            await message.channel.send('Bot already started!')


client.run(TOKEN)
