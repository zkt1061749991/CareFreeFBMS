# Generated by Django 2.0.7 on 2018-09-13 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProductDT', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_city',
            name='product_id',
            field=models.CharField(max_length=100, verbose_name='产品id'),
        ),
        migrations.AlterField(
            model_name='product_senic',
            name='product_id',
            field=models.CharField(max_length=100, verbose_name='产品id'),
        ),
        migrations.AlterField(
            model_name='product_senic',
            name='senic_name',
            field=models.CharField(max_length=100, verbose_name='景点名'),
        ),
    ]