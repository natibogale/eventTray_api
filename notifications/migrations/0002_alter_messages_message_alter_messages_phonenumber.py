# Generated by Django 4.0.4 on 2022-06-13 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='message',
            field=models.TextField(verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='phoneNumber',
            field=models.CharField(max_length=15, verbose_name='Phone Number'),
        ),
    ]
