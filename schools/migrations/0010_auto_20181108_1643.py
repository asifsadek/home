# Generated by Django 2.1.2 on 2018-11-08 11:13

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0009_school_descqription1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='descqription1',
            field=tinymce.models.HTMLField(blank=True, max_length=1000, null=True),
        ),
    ]