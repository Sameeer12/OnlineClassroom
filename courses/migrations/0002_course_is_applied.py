# Generated by Django 2.2 on 2019-04-16 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_applied',
            field=models.BooleanField(default=False),
        ),
    ]
