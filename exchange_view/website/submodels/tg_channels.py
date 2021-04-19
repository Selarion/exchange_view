from django.db import models


class TgChannel(models.Model):
    name = models.CharField(max_length=255)

    channel_id = models.BigIntegerField()
    real_id = models.IntegerField()

    is_channel = models.BooleanField()
    is_group = models.BooleanField()
    is_user = models.BooleanField()

    observing = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
