# Generated by Django 4.0.1 on 2022-03-30 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tblog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default=''),
        ),
    ]