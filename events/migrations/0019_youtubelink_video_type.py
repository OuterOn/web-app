# Generated by Django 2.1 on 2018-12-27 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0018_auto_20181226_1957'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtubelink',
            name='video_type',
            field=models.CharField(choices=[('USER_PERFORMANCE', 'User Performance'), ('GUEST_PERFORMANCE', 'Guest Performance'), ('IN_HOUSE', 'In House')], default='GUEST_PERFORMANCE', max_length=20),
            preserve_default=False,
        ),
    ]
