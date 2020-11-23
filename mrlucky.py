from telethon import TelegramClient, events
import time
import random
import asyncio
from datetime import datetime


status = False
min_limit = '37'
max_limit = '54'
previous = datetime.now()
previous_lvl = previous
level = 46
hp = '❤️Hp: 956/1102'

dicty = {}
msg_pays = ""
txt = '''
        💸💸💸**PAYTIME!!!**💸💸💸

Welcome, to the **Shack Lucky's Wizard Wheezes**
[/ws_mxRn3](http://t.me/share/url?url=/ws_mxRn3)

'''

loop = asyncio.get_event_loop()



api_id = id
api_hash = hash
phone = phon
bot_token = token

client=TelegramClient(phone,api_id,api_hash)
bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

client.start()

#Chat Wars events
@client.on(events.NewMessage(chats=('chtwrsbot'), incoming = True))
async def my_event_handler(event):
    global previous_lvl
    global level
    global max_limit
    global min_limit
    global hp
    global status
    global dicty
    global msg_pays
    if 'You were strolling around on your horse when you noticed' in event.raw_text:
        time.sleep(random.randint(3, 50))
        buttons = await event.get_buttons() 
        for bline in buttons: 
            for button in bline: 
                if 'Intervene' in button.button.text: 
                    await button.click() 
        await client.send_message('Mr_Lucky_Bot', 'The Intervene just arrived, go for it 🧹')
        time.sleep(3)
    elif '📖More info about the games basics can be found at' in event.raw_text:
        await client.send_message('Mr_Lucky_Bot', 'Testing foray script...')
    elif "This is sad but You are nearly dead." in event.raw_text:
        status = False
    elif "Battle of the seven castles in" in event.raw_text:
        msg = event.raw_text
        msg = msg.splitlines()
        for line in msg:
            if line.find("🏅Level:") != -1:
                level = int(line.lstrip("🏅Level: "))
                max_limit = str(level + 8)
                min_limit = str(level - 9)
            if line.find("❤️Hp") != -1:
                hp = line
                life = hp.lstrip('❤️Hp: ')
                life = life.split('/')
                life = life[0]
                if int(life) < 400:
                    status = False                
    elif event.sticker:
        now = datetime.now()
        prev = lastDate("levelup.txt")
        dif = now - prev
        nowDate(now, "levelup.txt")
        level = level + 1
        await event.forward_to('https://t.me/joinchat/AAAAAFLTi-nCB8VM0i8Cfw')
        time.sleep(0.5)
        await client.send_message('https://t.me/joinchat/AAAAAFLTi-nCB8VM0i8Cfw', """\
🌟Congratulations! New level!🌟\n
🐉[BKB]Mr Lucky Knight of Dragonscale
🏅Level: """ + str(level) + """
⌛️Date: """ + now.strftime("%d/%m/%Y %H:%M:%S") + """
⏳Time spent leveling up: """ + str(dif).split('.', 2)[0] + """
#lvlup""")
    elif 'has ordered' in event.raw_text:
        if msg_pays != "":
            msg = event.raw_text.split('has ordered')
            name = msg[0]
            name = name[4:]
            cash = msg[1]
            cash = cash.split('for')
            cash = cash[1]
            payed = int(cash[:-2])
            if name in dicty:
                dicty[name] = dicty[name] + payed
            else:
                dicty[name] = payed
            pays = ""
            total = 0
            for user in dicty:
                pays = pays + user + "—> 💰" + str(dicty[user]) + "\n"
                total = total + dicty[user]
            await client.edit_message('https://t.me/joinchat/AAAAAEuzn6lbbeEtu67a-w', msg_pays, txt + pays + "\nTotal: 💰" + str(total))
    

               
#Mobs event...Group mobs lvl 50+
@client.on(events.NewMessage(chats=('threebears'), incoming = True))
async def my_event_highgroup(event4):
    if status:
        if 'You met some hostile creatures.' in event4.raw_text:
            msg = event4.raw_text
            print(msg)
            msg = msg.splitlines()
            if verify(msg[1:-2]):
                print('Mob Accepted')
                code = msg.pop()
                print('Fight code: ' + code + '\n--------------------------------------------------')
                time.sleep(random.uniform(1.1, 1.4))
                await client.send_message('chtwrsbot', code)    
            else:
                print('Mob Rejected\n--------------------------------------------------')

#Mobs event...Chumlee pv
@client.on(events.NewMessage(chats=('PareceFalso'), incoming = True))
async def my_event_alexmobs(event5):
    if 'You met some hostile creatures.' in event5.raw_text:
        msg = event5.raw_text
        msg = msg.splitlines()
        if verify(msg[1:-2]):
            code = msg.pop()
            time.sleep(random.uniform(0.5, 0.9))
            await client.send_message('chtwrsbot', code)
            await client.send_message('PareceFalso', "OKKKK") 


def verify(mob):
    count_bad = 0
    count = 0
    for line in mob:
        line = line[-2:]
        if line.isdigit():
            count = count + 1
            if line < min_limit or line > max_limit:
                count_bad = count_bad + 1
                
    print('\nTotal differnt levels: ', count, '\nOut of range: ', count_bad)
    if count_bad == count:
        return False
    else:
        return True


#Bot code
@bot.on(events.NewMessage)
async def any_message_arrived_handler(event):
    global status
    global previous
    global max_limit
    global min_limit
    global dicty
    global msg_pays
    msg = event.raw_text
    chat_id = event.chat_id
    sender = await event.get_sender()
    name = sender.first_name
    print(chat_id)
    if chat_id != 720156493:
        await event.reply("Sorry pal, I only have permission to speak with my master. I can't be of any help to you... 😅")
    else:
        print(sender.username)
        print(name)
        if '/start' == event.raw_text:
            await event.reply("""\
Hello there """ + name + """, I'm Just A Rather Very Intelligent System (J.A.R.V.I.S)
and I'm here to help you with those scripts.
For more info press /help
""")
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
        elif '/status' == event.raw_text:
            if status:
                st = 'ON ✅'
            else:
                st = 'OFF ⛔️'
            await event.reply("""\
🐉[BKB]Mr Lucky
🏅Level: """ + str(level) + """\n""" + hp + """

Hunting status: """ + st + """
Minimum level of mobs accepted: """ + min_limit + """
Maximum level of mobs accepted: """ + max_limit)
        elif '/set_off' == event.raw_text:
            status = False
            await event.reply("The Hunt script is now out of service.\nPress /set_on to activate again.\n👾👾👾")
        elif '/set_on' == event.raw_text:
            status = True
            await event.reply("Open season! You are ready to hunt\nGood luck!!!\n🔪🐗")
        elif '/intervene' == event.raw_text:
            now = datetime.now()
            prev = lastDate("intervene.txt")
            dif = now - prev
            await event.reply('⌛️Last Intervene date: '+ prev.strftime("%d/%m/%Y %H:%M:%S") +'\n⏳Time since then: ' + str(dif).split('.', 2)[0])
        elif 'Testing foray script...' == event.raw_text:
            await event.reply( "Foray Script running OK 🤪")
        elif 'The Intervene just arrived, go for it 🧹' == event.raw_text:
            now = datetime.now()
            prev = lastDate("intervene.txt")
            dif = now - prev
            await event.reply("Intervene Recorded 🛡\n" + now.strftime("%d/%m/%Y %H:%M:%S") + '  \n\nPrevious Intervene: ' + prev.strftime("%d/%m/%Y %H:%M:%S") + '\nDifference from previous: ' + str(dif).split('.', 2)[0])
            nowDate(now, "intervene.txt")
        elif '/min_limit' in event.raw_text:
            min_limit = event.raw_text.lstrip("/min_limit ")
            await event.reply('Lower limit changed to ' + min_limit)
        elif '/max_limit' in event.raw_text:
            max_limit = event.raw_text.lstrip("/max_limit ")
            await event.reply('Upper limit changed to ' + max_limit)
        elif '/paytime' in event.raw_text:
            await event.reply("💸💸💸**PAYTIME!!!**💸💸💸")
            await client.send_message('chtwrsbot', '/myshop_open')
            mess = await client.send_message('https://t.me/joinchat/AAAAAEuzn6lbbeEtu67a-w', txt)
            msg_pays = mess.id
        elif msg == '/stoppay':
            await event.reply("Successfully funded!")
            dicty = {}
            msg_pays = ""
        else:
            await event.reply("ಠ‿ಠ")


def lastDate(txt):
    f = open(txt, "r")
    l = f.readlines()
    f.close()
    print(l)
    last = l[-1]
    last = last[0:26]
    print(last)
    prev = datetime.strptime(last, '%d/%m/%Y %H:%M:%S.%f')
    print('Previous: ', prev.strftime("%d/%m/%Y %H:%M:%S"))
    return prev

def nowDate(now,txt):
    f = open(txt, "a")
    f.write(now.strftime("%d/%m/%Y %H:%M:%S.%f") + '\n')
    f.close()


        

loop.run_forever()
