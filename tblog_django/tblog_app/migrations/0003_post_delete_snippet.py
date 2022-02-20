# Generated by Django 4.0.1 on 2022-02-20 08:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tblog_app', '0002_alter_snippet_options_snippet_highlighted_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=4096)),
                ('body', models.TextField(default='')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='Snippet',
        ),
    ]
