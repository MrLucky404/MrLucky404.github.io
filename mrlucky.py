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
  8: "Lo único que se es que es gay 🏳‍🌈🏳‍🌈🏳‍🌈.",
  9: "Solo se que por aquí alguien es 🦆...",
  10: "WTF!!!!",
  11: "Rómpete Mochiiiiiii!!!",
  12: "Al igual que tú",
  13: "OOhh yeaaa",
}

#Bot code
@bot.on(events.NewMessage)
async def any_message_arrived_handler(event):
    msg = event.raw_text
    chat_id = event.chat_id
    sender = await event.get_sender()
    name = sender.first_name
    if '/start' == event.raw_text:
            await event.reply("Hello there " + name)
    elif "/slap" == msg:
        await event.reply("🍑")
    elif "hola" in msg or "Hola" in msg or "Hello" in msg:
        await event.reply("Hola guap@ 🌚🌚")
    elif "/siono" in msg:
        if "/siono" == msg:
            await event.reply("¿Cúal es la pregunta genio, ahora tengo que ser adivino?")
        else:
            op = random.randint(1,13)
            answ = siono[op]
            await event.reply(answ)

        

loop.run_forever()
