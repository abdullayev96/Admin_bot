# Generated by Django 4.1.4 on 2023-01-05 05:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0020_orderproduct_alter_product_options_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.DeleteModel(
            name='OrderProduct',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'managed': False, 'verbose_name': "O'quv kurs", 'verbose_name_plural': "O'quv kurslar"},
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
