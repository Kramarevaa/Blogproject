# Generated by Django 3.1.4 on 2021-01-02 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='comments',
            field=models.ManyToManyField(blank=True, to='comments.Comment'),
        ),
    ]
