# Generated by Django 4.0.4 on 2022-05-13 17:58

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import location_field.models.plain
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Venues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(max_length=250, verbose_name='Venue')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='Venue Image/', verbose_name='Venue Image')),
            ],
            options={
                'verbose_name_plural': 'Venues',
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventName', models.CharField(max_length=250, verbose_name='Event Name')),
                ('eventDescription', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Event Description')),
                ('eventCategory', multiselectfield.db.fields.MultiSelectField(choices=[('Activities', 'Activities'), ('Art', 'Art'), ('Bazar', 'Bazar'), ('Business', 'Business'), ('Concert', 'Concert'), ('Conference', 'Conference'), ('Dance', 'Dance'), ('Education', 'Education'), ('Exhibition', 'Exhibition'), ('Expo', 'Expo'), ('Fashion', 'Fashion'), ('Festival', 'Festival'), ('Film', 'Film'), ('Food', 'Food'), ('Fundraiser', 'Fundraiser'), ('Music', 'Music'), ('Online Webinar', 'Online Webinar'), ('Night Life', 'Night Life'), ('Sports', 'Sports'), ('Technology', 'Technology'), ('Travel', 'Travel'), ('Training', 'Training')], max_length=184, verbose_name='Event Category')),
                ('eventStartDate', models.DateField(verbose_name='Event Start Date')),
                ('eventEndDate', models.DateField(verbose_name='Event End Date')),
                ('eventStartTime', models.TimeField(verbose_name='Event Start Time')),
                ('eventEndTime', models.TimeField(verbose_name='Event End Time')),
                ('eventLocation', location_field.models.plain.PlainLocationField(blank=True, max_length=63, null=True, verbose_name='Event Location')),
                ('eventType', models.CharField(choices=[('In Person', 'In Person'), ('Online', 'Online')], max_length=250, verbose_name='Event Type')),
                ('venue', models.CharField(max_length=250, verbose_name='Venue')),
                ('eventCity', models.CharField(max_length=250, verbose_name='Event City')),
                ('eventCountry', models.CharField(default='Ethiopia', max_length=250, verbose_name='Event Country')),
                ('is_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_cancelled', models.BooleanField(default=False)),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Events',
            },
        ),
    ]