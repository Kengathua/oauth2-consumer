# Generated by Django 4.0.3 on 2022-06-05 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='guid',
            field=models.UUIDField(blank=True, null=True, unique=True),
        ),
    ]
