# Generated by Django 4.0.4 on 2022-05-14 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_organizer_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizer',
            name='displayName',
            field=models.CharField(help_text='A name you want Customers to identify your business by / For organizations input the name of your organization.', max_length=150, verbose_name='Business Display Name'),
        ),
    ]
