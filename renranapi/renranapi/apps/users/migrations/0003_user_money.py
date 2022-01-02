# Generated by Django 3.2.10 on 2022-01-02 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='money',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='用户资金'),
        ),
    ]