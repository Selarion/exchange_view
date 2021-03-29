from django.db import models


class TgMessage(models.Model):
    raw_text = models.TextField()
