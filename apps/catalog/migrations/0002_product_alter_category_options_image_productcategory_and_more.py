# Generated by Django 5.0.2 on 2024-04-11 17:19

import apps.catalog.models
import django.db.models.deletion
import imagekit.models.fields
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Назва')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Опис')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Кількість')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Ціна')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товари',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['title'], 'verbose_name': 'Категорія', 'verbose_name_plural': 'Категорії'},
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=apps.catalog.models.get_image_path, verbose_name='Зображення')),
                ('is_main', models.BooleanField(default=False, verbose_name='Основне зображення')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='catalog.product', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'Зображення',
                'verbose_name_plural': 'Зображення',
                'ordering': ['product', '-is_main'],
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main', models.BooleanField(default=False, verbose_name='Основна категорія')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
            ],
            options={
                'verbose_name': 'Категорія товару',
                'verbose_name_plural': 'Категорії товарів',
                'unique_together': {('product', 'category')},
            },
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='products', through='catalog.ProductCategory', to='catalog.category', verbose_name='Категорії'),
        ),
    ]
