# Generated by Django 4.0.3 on 2022-04-07 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
