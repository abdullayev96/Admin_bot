# Generated by Django 4.1.4 on 2022-12-24 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0015_auto_20211202_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
