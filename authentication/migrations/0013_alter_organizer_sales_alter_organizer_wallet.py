# Generated by Django 4.0.4 on 2022-06-14 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_organizer_wallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizer',
            name='sales',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Total Sales'),
        ),
        migrations.AlterField(
            model_name='organizer',
            name='wallet',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Wallet'),
        ),
    ]