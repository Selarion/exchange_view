
# Remember to use your own values from my.telegram.org!
from telethon import TelegramClient, events

from tg_parser.config import *

api_id = API_ID
api_hash = API_HASH
client = TelegramClient('anon_parser_channels', api_id, api_hash)


# noinspection PyTypeChecker
@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'hello' in event.raw_text:
        await event.reply('hi!')
    print(event)

if __name__ == '__main__':
    client.start()
    client.run_until_disconnected()
