# Generated by Django 4.1.3 on 2022-11-17 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_restaurant_delivery'),
    ]

    operations = [
        migrations.RenameField(
            model_name='restaurant',
            old_name='cpnj',
            new_name='cnpj',
        ),
    ]
