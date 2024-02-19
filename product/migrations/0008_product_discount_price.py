# Generated by Django 4.2.9 on 2024-02-19 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_productstatus_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Discount Price'),
        ),
    ]