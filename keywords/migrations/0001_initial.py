# Generated by Django 5.1.5 on 2025-02-12 23:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(default='', max_length=10, unique=True)),
                ('category', models.CharField(choices=[('emotion', 'Emotion'), ('weather', 'Weather'), ('situation', 'Situation'), ('genre', 'Genre')], default='emotion', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('artist', models.CharField(max_length=20)),
                ('youtube_url', models.URLField(default='', null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song_Keyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='keywords.keyword')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='keywords.song')),
            ],
        ),
        migrations.AddField(
            model_name='song',
            name='keywords',
            field=models.ManyToManyField(through='keywords.Song_Keyword', to='keywords.keyword'),
        ),
    ]
