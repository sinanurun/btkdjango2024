# Generated by Django 5.0.2 on 2024-03-03 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_category_level_category_lft_category_rght_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='reviewsCount',
            field=models.IntegerField(default=0),
        ),
    ]
