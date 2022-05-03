# Generated by Django 4.0.4 on 2022-05-02 08:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Directorates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directorate', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Directorates',
            },
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('username', models.CharField(max_length=500, unique=True, verbose_name='Badge Number')),
                ('firstName', models.CharField(blank=True, max_length=500, verbose_name='First Name')),
                ('middleName', models.CharField(blank=True, max_length=500, verbose_name='Middle Name')),
                ('lastName', models.CharField(blank=True, max_length=500, verbose_name='Last Name')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=100, verbose_name='Gender')),
                ('email', models.CharField(max_length=500, unique=True, verbose_name='Email')),
                ('phoneNumber', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Please enter your phonenumber in the format starting with: 09 or +251', regex='^\\+?1?\\d{10,15}$')], verbose_name='Phone Number')),
                ('title', models.CharField(blank=True, choices=[('Director', 'Director'), ('Team Leader', 'Team Leader'), ('Office Assistant', 'Office Assistant'), ('Lead Engineer', 'Lead Engineer'), ('Record Officer', 'Record Officer'), ('Project Engineer', 'Project Engineer'), ('Secretary', 'Secretary'), ('HR Officer', 'HR Officer')], max_length=100, verbose_name='Title')),
                ('emergencyContactName', models.CharField(blank=True, max_length=500, verbose_name='Emergency Contact Name')),
                ('emergencyContactPhone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Please enter your phonenumber in the format starting with: 09 or +251', regex='^\\+?1?\\d{10,15}$')], verbose_name='Emergency Contact Phone')),
                ('profilePicture', models.ImageField(default='Profile_Pictures/default.png', upload_to='Profile_Pictures/', verbose_name='Profile Picture')),
                ('lastEdit', models.DateTimeField(auto_now=True, verbose_name='Last Edit')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('directorate', models.ForeignKey(blank=True, default=1, max_length=500, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.directorates', verbose_name='Directorate')),
                ('team', models.ForeignKey(blank=True, default=1, max_length=500, null=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.teams', verbose_name='Team')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
