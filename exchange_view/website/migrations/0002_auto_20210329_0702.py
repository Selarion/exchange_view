# Generated by Django 3.1.7 on 2021-03-29 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TgChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_id', models.IntegerField()),
                ('title', models.CharField(max_length=255)),
                ('is_channel', models.BooleanField()),
                ('is_group', models.BooleanField()),
                ('is_user', models.BooleanField()),
            ],
        ),
        migrations.RenameModel(
            old_name='TgMessages',
            new_name='TgMessage',
        ),
        migrations.DeleteModel(
            name='TgChannels',
        ),
    ]
