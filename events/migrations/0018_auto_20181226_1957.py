# Generated by Django 2.1 on 2018-12-26 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_auto_20181226_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['datetime']},
        ),
    ]
