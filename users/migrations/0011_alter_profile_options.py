# Generated by Django 4.1.4 on 2023-04-08 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_rename_e_mail_profile_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['created']},
        ),
    ]
