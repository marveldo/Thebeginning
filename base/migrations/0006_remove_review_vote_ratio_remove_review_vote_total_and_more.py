# Generated by Django 4.1.4 on 2023-01-07 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_review_vote_ratio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='vote_ratio',
        ),
        migrations.RemoveField(
            model_name='review',
            name='vote_total',
        ),
        migrations.AddField(
            model_name='room',
            name='vote_ratio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='vote_total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]