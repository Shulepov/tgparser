from telethon import TelegramClient, events

app_id = 12639386
api_hash = '0b935c59441284d7ae831db87230255a'

#нарния чат -1001369370434
#lobsterdao -1001242127973
#defilog -1001451302716

forwardChat = -1001673311085

chats = [-1001369370434, -1001242127973, -1001451302716]

client = TelegramClient('user', app_id, api_hash)

@client.on(events.NewMessage)
async def my_event_handler(event):
    chat_id = event.chat_id
    if chat_id in chats:
        print(event.raw_text)
        await event.forward_to(forwardChat)

client.start()
client.run_until_disconnected()

#with TelegramClient('user', app_id, api_hash) as client:
    #client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))