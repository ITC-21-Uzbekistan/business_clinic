# Generated by Django 4.0.6 on 2022-08-03 10:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('direction', '0002_alter_directionmedicine_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('room_number', models.CharField(blank=True, max_length=100, null=True)),
                ('direction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='direction.directionmedicine')),
            ],
            options={
                'db_table': 'room',
            },
        ),
    ]