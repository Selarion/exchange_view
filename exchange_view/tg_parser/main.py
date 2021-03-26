from telethon.sync import TelegramClient, events

api_id = 3897302
api_hash = '80c0d39df47be95e09c329ee49bb88a5'


with TelegramClient('name', api_id, api_hash) as client:
    client.send_message('me', 'Hello, myself!')

    @client.on(events.NewMessage(pattern='(?i).*Hello'))
    async def handler(event):
        await event.reply('Hey!')

    client.run_until_disconnected()

# TODO
# Подумать, как это будет разворачиваться на новой машине в автоматическом
# режиме.
# Продумать механизм закачки сообщений в бд. Как сделать так,
# чтобы уже закаченные не грузили сервера телеграмма
#
# В конце концов получить БД с сообщениями
