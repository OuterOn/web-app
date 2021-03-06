# Generated by Django 2.1 on 2018-12-26 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_auto_20181226_0606'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveIntegerField(choices=[('1', '*'), ('2', '**'), ('3', '***'), ('4', '****'), ('5', '*****')])),
                ('comment', models.TextField()),
                ('event_person_map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.EventPersonMap')),
            ],
        ),
        migrations.AddField(
            model_name='youtubelink',
            name='tags',
            field=models.CharField(default='singing,music', help_text='separated tags with a comma.', max_length=100),
            preserve_default=False,
        ),
    ]
