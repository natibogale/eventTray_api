# Generated by Django 4.0.4 on 2022-06-13 16:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0010_ticketsbought_ticketname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketsbought',
            name='qrCode',
            field=models.CharField(default=uuid.uuid4, max_length=50, verbose_name='QR Code'),
        ),
    ]
