from django.db import models


class TgMessage(models.Model):

    raw_text = models.TextField()

    def __str__(self):
        return self.raw_text
