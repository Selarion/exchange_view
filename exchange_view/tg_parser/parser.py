from telethon.sync import TelegramClient as TelegramClientSync
from telethon import TelegramClient
# from tg_parser.config import API_ID, API_HASH


class TgParser(TelegramClient):
    def __init__(self, *args, **kwargs):
        self.api_id = API_ID
        self.api_hash = API_HASH
        super(TgParser, self).__init__(
            session='anon_parse_channels',
            api_id=self.api_id,
            api_hash=self.api_hash,
            *args, **kwargs
        )

    # noinspection PyTypeChecker
    def get_channels(self, and_me=False):
        """
        Download all Dialogs from Tg and filter it by channels only.
        and_me - add myself chat into result
        """
        dialogs = [d for d in self.get_dialogs()]
        channels = list(filter(lambda d: d.is_channel, dialogs))
        if not and_me:
            channels.append(client.get_me())
        return channels


async def main(client):
    for c in [1, 2, 3, 4, 5]:
        client.loop.create_task(foo(c))


async def foo(x):
    print(x)
    await asyncio.sleep(random.randint(0, 3))


if __name__ == '__main__':
    import random
    import sys
    import time
    import asyncio

    sys.path[0] = ''
    from tg_parser.config import API_ID, API_HASH

    client = TgParser()
    with client:
        client.loop.run_until_complete(main(client))

    # channels = client.get_channels()
    # channel_ids = [c.id for c in channels]

    # msg = client.get_messages(channels[0].id, limit=10)
    # time.sleep(4)
    # channels = client.get_channels()
    # print(channels)
