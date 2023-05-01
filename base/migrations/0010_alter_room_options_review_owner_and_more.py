# Generated by Django 4.1.4 on 2023-04-08 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_profile_options'),
        ('base', '0009_room_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['created']},
        ),
        migrations.AddField(
            model_name='review',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('owner', 'room_name')},
        ),
    ]