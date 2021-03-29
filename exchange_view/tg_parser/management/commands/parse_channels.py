from django.core.management.base import BaseCommand, CommandError
from tg_parser.parser import parse
from website.models import TgChannel


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        try:
            tg_channels = parse()
            for c in tg_channels:

                chnl, created = TgChannel.objects.get_or_create(
                    channel_id=c.entity.id,
                    title=c.entity.title,
                    is_channel=c.is_channel,
                    is_user=c.is_user,
                    is_group=c.is_group
                )
                if created:
                    print(f'new row: {c.entity.title}')

        except Exception as e:
            raise CommandError(e)
