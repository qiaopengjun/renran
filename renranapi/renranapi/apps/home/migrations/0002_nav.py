# Generated by Django 3.2.10 on 2021-12-27 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orders', models.IntegerField(blank=True, default=0, null=True, verbose_name='排序')),
                ('is_show', models.BooleanField(default=True, verbose_name='是否显示')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='是否删除')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=150, verbose_name='导航名称')),
                ('icon', models.CharField(help_text='这里填写的是样式名称.', max_length=150, verbose_name='icon图标')),
                ('link', models.CharField(blank=True, max_length=150, null=True, verbose_name='导航地址')),
                ('position', models.IntegerField(choices=[(1, '头部导航'), (2, '脚部导航')], default=1, verbose_name='导航位置')),
                ('is_http', models.BooleanField(default=False, help_text='站内地址格式：/users/<br>站外地址格式：http://www.baidu.com', verbose_name='是否站外地址')),
                ('pid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='son', to='home.nav', verbose_name='父亲导航')),
            ],
            options={
                'verbose_name': '导航菜单',
                'verbose_name_plural': '导航菜单',
                'db_table': 'rr_nav',
            },
        ),
    ]
