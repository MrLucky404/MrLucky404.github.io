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

#Bot code
@bot.on(events.NewMessage)
async def any_message_arrived_handler(event):
    msg = event.raw_text
    chat_id = event.chat_id
    sender = await event.get_sender()
    name = sender.first_name
    if '/start' == event.raw_text:
            await event.reply("""\
Hello there """ + name + """, I'm F.R.Y.D.A.Y"""
    elif '/help' == event.raw_text:
        await event.reply("""\
List of commands available:
/set_off - Disable hunt script\n/set_on - Enable hunt script
/intervene - View last intervene date
/status - View Hunt Script status
/min_limit [level] - Set minimum level of mobs accepted
/max_limit [level] - Set maximum level of mobs accepted

*to check that the intervene script is running correctly type /help in @chtwrsbot
""")
    else:
        await event.reply(msg)

        

loop.run_forever()
