# Generated by Django 4.0.6 on 2022-07-22 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('rainfall', models.ImageField(upload_to='')),
            ],
        ),
    ]
