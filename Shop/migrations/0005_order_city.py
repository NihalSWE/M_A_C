# Generated by Django 4.2.7 on 2023-11-20 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(default='', max_length=50),
        ),
    ]
