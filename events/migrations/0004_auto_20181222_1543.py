# Generated by Django 2.1 on 2018-12-22 15:43

from django.db import migrations, models
import django.db.models.deletion
import events.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20181222_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=events.models.gallery_directory_path)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
        migrations.AddField(
            model_name='performerdetail',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
