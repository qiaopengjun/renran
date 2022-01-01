# Generated by Django 3.2.10 on 2022-01-01 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0003_articlepostspecial_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepostspecial',
            name='special',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myarticles', to='article.articlespecial', verbose_name='专题'),
        ),
        migrations.AlterField(
            model_name='articlepostspecial',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '投稿中'), (1, '等待审核'), (2, '审核通过'), (3, '审核不通过')], default=0, verbose_name='审核状态'),
        ),
        migrations.AlterField(
            model_name='specialmanager',
            name='special',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mymanager', to='article.articlespecial', verbose_name='专题'),
        ),
    ]
