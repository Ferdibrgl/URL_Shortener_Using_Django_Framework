# Generated by Django 3.1 on 2020-08-30 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('router', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='short_url',
            field=models.TextField(),
        ),
    ]
