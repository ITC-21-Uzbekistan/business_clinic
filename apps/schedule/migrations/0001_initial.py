# Generated by Django 4.0.6 on 2022-08-03 10:48

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('room', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('finish_time', models.TimeField(blank=True)),
                ('start_lunch', models.TimeField(blank=True, default=datetime.time(13, 0))),
                ('finish_lunch', models.TimeField(blank=True, default=datetime.time(14, 0))),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='room.room')),
            ],
            options={
                'db_table': 'schedule',
            },
        ),
    ]
