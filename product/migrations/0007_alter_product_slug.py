# Generated by Django 5.0.2 on 2024-03-10 12:53

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title'),
        ),
    ]
