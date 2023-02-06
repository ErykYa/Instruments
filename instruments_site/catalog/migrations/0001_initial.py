# Generated by Django 4.1 on 2022-08-10 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Наименование')),
                ('code', models.IntegerField(unique=True, verbose_name='Код')),
                ('vendor_code', models.CharField(max_length=100, verbose_name='Артикул')),
                ('brand', models.CharField(max_length=100, verbose_name='Бренд')),
                ('availability', models.CharField(max_length=100, verbose_name='Наличие')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='Цена из парсинга')),
                ('img_url', models.URLField(verbose_name='Фото')),
            ],
        ),
    ]