# Generated by Django 3.2.10 on 2021-12-29 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_nav'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='info',
            field=models.TextField(blank=True, null=True, verbose_name='备注信息'),
        ),
    ]
