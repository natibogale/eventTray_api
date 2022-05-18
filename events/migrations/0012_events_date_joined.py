# Generated by Django 4.0.4 on 2022-05-15 08:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_remove_events_eventcategories_events_eventcategories'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Date Created'),
            preserve_default=False,
        ),
    ]
