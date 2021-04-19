from django.core.management.base import BaseCommand
from telethon import utils

from tg_parser.parser import TgParser
from website.models import TgChannel


class Command(BaseCommand):
    help = 'Скачивает из телеграмма и сохраняет в БД все калаы и сообщения.'

    def handle(self, *args, **options):
        parser = TgParser()

        #  Скачиваем и сохраняем каналы из телеграмма.
        print('Channels...')
        channels = parser.loop.run_until_complete(parser.get_channels())
        for ch in channels:
            real_id, peer_type = utils.resolve_id(ch.id)
            TgChannel.objects.get_or_create(
                name=ch.name, channel_id=int(ch.id), real_id=real_id,
                is_channel=ch.is_channel, is_user=ch.is_user, is_group=ch.is_group
            )

        #  Скачиываем и сохраняем сообщения их этих каналов
        print('Messages...')
        massages = parser.loop.run_until_complete(
            parser.get_messages_by_channels(channels, limit=100, reverse=True, wait_time=1)
        )



    # @staticmethod
    # def _save_channels(channels):
    #     print('Creating channels...')
    #     for c in channels:
    #         real_id, peer_type = utils.resolve_id(c.id)
    #         chnl, created = TgChannel.objects.get_or_create(
    #             name=c.name,
    #             channel_id=int(c.id), real_id=real_id,
    #             is_channel=c.is_channel, is_user=c.is_user, is_group=c.is_group
    #         )
            # if created:
            #     print(f'new row: {c.name}')
            # else:
            #     print(f'{c.name} - is already exist.')

    def _save_messages(self, messages):
        pass
