# Generated by Django 4.2.1 on 2023-05-30 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0003_alter_watchdata_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
