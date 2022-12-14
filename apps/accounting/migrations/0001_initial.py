# Generated by Django 4.0.6 on 2022-08-02 08:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accounting',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('account_date', models.DateField(blank=True, default=None, null=True)),
                ('total_amount', models.FloatField(blank=True, default=0, null=True)),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='service.service')),
            ],
            options={
                'db_table': 'accounting',
                'ordering': ['id'],
            },
        ),
    ]
