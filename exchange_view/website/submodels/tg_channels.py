from django.db import models


class TgChannel(models.Model):
    channel_id = models.IntegerField()
    title = models.CharField(max_length=255)
    is_channel = models.BooleanField()
    is_group = models.BooleanField()
    is_user = models.BooleanField()
