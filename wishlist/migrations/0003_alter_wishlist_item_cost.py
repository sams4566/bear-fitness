# Generated by Django 3.2 on 2022-01-04 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wishlist', '0002_rename_item_size_wishlist_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='item_cost',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
