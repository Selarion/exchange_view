from django.db import models


class TgMessages(models.Model):
    raw_text = models.TextField()
