from telethon.sync import TelegramClient
from tg_parser.telegram_token import API_ID, API_HASH


# noinspection PyTypeChecker
def parse():
    client = TelegramClient('anon_parser_channels', API_ID, API_HASH).start()

    all_dialogs = [d for d in client.get_dialogs()]
    only_channels = list(filter(lambda d: d.is_channel, all_dialogs))

    return only_channels


if __name__ == '__main__':
    parse()

"""
TODO:
- конфиги тг-клиента вынести в отдельную директорию
- Установить единую директорию для .sessions, чтобы не плодить этих сущностей.
"""
