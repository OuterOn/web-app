# Generated by Django 2.1 on 2018-12-26 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_auto_20181226_0714'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='one_liner',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.PositiveIntegerField(choices=[(1, '*'), (2, '**'), (3, '***'), (4, '****'), (5, '*****')]),
        ),
    ]
