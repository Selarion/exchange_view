import asyncio
from pathlib import Path

from telethon import TelegramClient

from tg_parser.config import API_ID, API_HASH, SESSION_NAME


class TgParser(TelegramClient):
    def __init__(self, *args, **kwargs):
        self.api_id = API_ID
        self.api_hash = API_HASH
        session_path = str(Path(__file__).resolve().parent / SESSION_NAME)
        super(TgParser, self).__init__(
            session=session_path,
            api_id=self.api_id,
            api_hash=self.api_hash,
            *args, **kwargs
        )
        self.start()

    # noinspection PyTypeChecker
    async def get_channels(self, *args, **kwargs):
        """
        Download all Dialogs from Tg and filter by channels only.
        and_me - add myself chat into result
        """
        dialogs = self.iter_dialogs(*args, **kwargs)
        channels = list(filter(lambda x: x.is_channel, [d async for d in dialogs]))

        return channels

    async def get_messages_by_channels(self, channels, *args, **kwargs):
        tasks = []
        for c in channels:
            tasks.append(asyncio.create_task(self._get_messages(c, *args, **kwargs)))
        messages = [await t for t in tasks]
        print(messages)

    async def _get_messages(self, channel, *args, **kwargs):
        messages = []
        async for m in self.iter_messages(channel, *args, **kwargs):
            print(f'{channel.name} - {m.id}')
            messages.append(m)
        return channel, messages




# def main():
#     client = TgParser()
#     channels = client.loop.run_until_complete(client.get_channels())
#     print(channels)
#     print('finish')
#
#
# if __name__ == '__main__':
#     import random
#     import sys
#     import asyncio
#
#     sys.path[0] = ''
#     from tg_parser.config import API_ID, API_HASH, SESSION_NAME
#     main()
