# Generated by Django 4.0.4 on 2022-05-29 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0019_alter_events_eventlocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='expired',
            field=models.BooleanField(default=False),
        ),
    ]