# Generated by Django 4.0.4 on 2022-06-13 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0014_ticketsbought_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketsbought',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='merchs/'),
        ),
    ]
