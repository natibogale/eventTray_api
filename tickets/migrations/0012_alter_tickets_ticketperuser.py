# Generated by Django 4.0.4 on 2022-06-13 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0011_alter_ticketsbought_qrcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='ticketPerUser',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Ticket Sell per User'),
        ),
    ]