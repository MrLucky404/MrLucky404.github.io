from telethon import TelegramClient, events
import time
import random
import asyncio
from datetime import datetime


loop = asyncio.get_event_loop()


api_id = 1616250
api_hash = '682ffddbc0261eb1bc65d5bcdec9faf0'
bot_token = '1329256652:AAHLjEfCHR2J21y54_hQ2RYjx8zQxmGHoSM'

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

bot.start()

siono = {
  1: "Si",
  2: "No",
  3: "Umju",
  4: "Es difícil dar una respuesta exacta, creo que debemos tomar la pregunta con cautela y analizar los pormenores que pueden parecernos intrascendentes pero que, a la hora de tomar una decisión coherente, pueden torcer la balanza.",
  5: "Me atrevo a decir que si.",
  6: "La mayoría de las veces recurre a ese tipo de prácticas.",
  7: "Ni loco.",
  8: "Lo único que se es que es gay 🏳‍🌈🏳‍🌈🏳‍🌈."
}

#Bot code
@bot.on(events.NewMessage)
async def any_message_arrived_handler(event):
    msg = event.raw_text
    chat_id = event.chat_id
    sender = await event.get_sender()
    name = sender.first_name
    if '/start' == event.raw_text:
            await event.reply("""\
Hello there """ + name + """)
    elif "@coffee_breaks_bot" in msg:
        await event.reply("Que tu quieres?")
    elif "/slap" == msg:
        await event.reply("🍑")
    elif "/siono" in msg:
        op = random.randint(0,8)
        answ = siono[op]
        await event.reply(answ)
    else:
        await event.reply(msg)

        

loop.run_forever()
