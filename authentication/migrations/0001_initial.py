# Generated by Django 4.0.4 on 2022-05-13 17:58

import authentication.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=500, unique=True, verbose_name='User Name')),
                ('firstName', models.CharField(blank=True, max_length=500, verbose_name='First Name')),
                ('lastName', models.CharField(blank=True, max_length=500, verbose_name='Last Name')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=100, verbose_name='Gender')),
                ('phoneNumber', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(message='Please enter your phonenumber in the format starting with: 09', regex='^\\+?1?\\d{10}$')], verbose_name='Phone Number')),
                ('profilePicture', models.ImageField(default='Profile_Pictures/default.png', upload_to='Profile_Pictures/', verbose_name='Profile Picture')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Organizer Email')),
                ('counter', models.IntegerField(default=0)),
                ('role', models.CharField(blank=True, choices=[('User', 'User'), ('Organizer', 'Organizer'), ('Checker', 'Checker')], max_length=100, verbose_name='Role')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_authenticated', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', authentication.models.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('organizer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='Organizer')),
                ('displayName', models.CharField(help_text='Enter the name you want Customers to identify your business by.', max_length=150, verbose_name='Business Display Name')),
                ('organizerType', models.CharField(choices=[('Individual', 'Individual'), ('Organization', 'Organization')], default='Organization', max_length=150, verbose_name='Organizer Type')),
                ('twitter', models.CharField(blank=True, max_length=150, null=True, verbose_name='Twitter Link')),
                ('telegram', models.CharField(blank=True, max_length=150, null=True, verbose_name='Telegram Link')),
                ('facebook', models.CharField(blank=True, max_length=150, null=True, verbose_name='Facebook')),
                ('instagram', models.CharField(blank=True, max_length=150, null=True, verbose_name='Instagram Link')),
                ('verifyingDocument', models.FileField(blank=True, null=True, upload_to='Verifying_Document', verbose_name='Verifying Document')),
                ('verifiedOrganizer', models.BooleanField(default=False)),
                ('totalVisitors', models.CharField(blank=True, default=0, max_length=150, null=True, verbose_name='Total Visitors')),
                ('dailyVisitors', models.CharField(blank=True, default=0, max_length=150, null=True, verbose_name='Daily Visitors')),
                ('followers', models.CharField(blank=True, default=0, max_length=150, null=True, verbose_name='Followers')),
                ('events', models.CharField(blank=True, default=0, max_length=150, null=True, verbose_name='Total Events')),
                ('sales', models.CharField(blank=True, default=0, max_length=150, null=True, verbose_name='Total Sales')),
                ('tickets', models.CharField(blank=True, default=0, max_length=150, null=True, verbose_name='Sold Tickets')),
            ],
            options={
                'verbose_name_plural': 'Organizer Details',
            },
        ),
    ]
