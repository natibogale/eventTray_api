# Generated by Django 4.0.4 on 2022-05-20 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_remove_tickets_endsellon_remove_tickets_startsellon_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='price',
            field=models.FloatField(default=0, verbose_name='Price per Unit'),
        ),
    ]
