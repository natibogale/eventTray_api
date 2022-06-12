# Generated by Django 4.0.4 on 2022-06-12 11:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0022_events_image'),
        ('tickets', '0006_tickets_ticketowner'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketsBought',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.events', verbose_name='Event')),
            ],
            options={
                'verbose_name_plural': 'Tickets Bought',
            },
        ),
    ]
