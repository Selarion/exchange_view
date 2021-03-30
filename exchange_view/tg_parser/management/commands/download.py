from django.core.management.base import BaseCommand
from tg_parser.parser import TgParser


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        import os
        os.getcwd()
        print('!!!')
        parser = TgParser()
        print(parser.get_channels())

    @staticmethod
    def _download_channels():
        pass
        # tg_channels = all_tg_channels()
        # tg_channels = list(filter(
        #     lambda d: d.is_channel or d.name == 'Михаил Зверев',
        #     tg_channels
        # ))
        # for c in tg_channels:
        #
        #     chnl, created = TgChannel.objects.get_or_create(
        #         channel_id=c.entity.id,
        #         title=c.name,
        #         is_channel=c.is_channel,
        #         is_user=c.is_user,
        #         is_group=c.is_group
        #     )
        #     if created:
        #         print(f'new row: {c.name}')
        #     else:
        #         print(f'{c.name} - is already exist.')
