# Generated by Django 2.1.2 on 2018-11-06 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0003_auto_20181106_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='url_endpoint',
            field=models.SlugField(blank=True, null=True),
        ),
    ]