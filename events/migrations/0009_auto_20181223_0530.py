# Generated by Django 2.1 on 2018-12-23 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20181223_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='website',
            field=models.URLField(),
        ),
    ]
