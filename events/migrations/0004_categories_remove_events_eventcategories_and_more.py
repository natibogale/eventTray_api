# Generated by Django 4.0.4 on 2022-05-14 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_rename_eventcategory_events_eventcategories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=150, verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.RemoveField(
            model_name='events',
            name='eventCategories',
        ),
        migrations.AddField(
            model_name='events',
            name='eventCategories',
            field=models.ManyToManyField(to='events.categories', verbose_name='Event Category'),
        ),
    ]
