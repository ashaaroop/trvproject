# Generated by Django 4.1.3 on 2022-11-29 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo1app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('h1', models.CharField(max_length=250)),
                ('img1', models.ImageField(upload_to='pics')),
                ('des1', models.TextField()),
            ],
        ),
    ]
