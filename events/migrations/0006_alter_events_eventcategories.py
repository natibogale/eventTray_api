# Generated by Django 4.0.4 on 2022-05-14 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_remove_events_eventcategories_events_eventcategories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='eventCategories',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Event Category'),
        ),
    ]
