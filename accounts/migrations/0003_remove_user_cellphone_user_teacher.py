# Generated by Django 4.1 on 2022-09-28 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_profilepic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='cellphone',
        ),
        migrations.AddField(
            model_name='user',
            name='teacher',
            field=models.BooleanField(default=False),
        ),
    ]
