# Generated by Django 4.1.4 on 2023-03-13 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_profile_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='e_mail',
            new_name='email',
        ),
    ]