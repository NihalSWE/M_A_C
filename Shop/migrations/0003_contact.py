# Generated by Django 4.2.7 on 2023-11-13 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_product_category_product_image_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=20)),
                ('description', models.CharField(default='', max_length=300)),
            ],
        ),
    ]
