from telethon import TelegramClient, events
import re

app_id = 12983384
api_hash = '641d1d4b6b72e34e296f128ad84e4c97'
pattern = re.compile('(https?:\/\/.+?\.\w+)|(\w+\.(?:com|io|online|fi|org|ru|finance|fund|network|money|co|exchange|xyz|app|cash|ai))')

#нарния чат -1001369370434
#lobsterdao -1001242127973
#defilog -1001451302716

forwardChat = -1001773781316

chats = [-1001369370434, -1001242127973, -1001451302716]

client = TelegramClient('user', app_id, api_hash)

@client.on(events.NewMessage)
async def my_event_handler(event):
    chat_id = event.chat_id
    if chat_id in chats:
        if pattern.search(event.raw_text) is not None:
            print(event.raw_text)
            await event.forward_to(forwardChat)

client.start()
client.run_until_disconnected()

#with TelegramClient('user', app_id, api_hash) as client:
    #client.loop.run_until_complete(client.send_message('me', 'Hello, myself!'))