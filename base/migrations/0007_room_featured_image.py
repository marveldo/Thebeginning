# Generated by Django 4.1.4 on 2023-02-20 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_remove_review_vote_ratio_remove_review_vote_total_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='featured_image',
            field=models.ImageField(blank=True, default='guest-user.webp', null=True, upload_to=''),
        ),
    ]
