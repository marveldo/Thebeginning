# Generated by Django 4.1.4 on 2023-02-28 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.TextField(blank=True, max_length=150, null=True),
        ),
    ]
