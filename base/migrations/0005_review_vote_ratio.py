# Generated by Django 4.1.4 on 2023-01-06 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_review_vote_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='vote_ratio',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]