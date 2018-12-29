# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-18 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skyuser', '0002_auto_20171118_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datalist',
            name='data_file1',
            field=models.FileField(blank=True, null=True, upload_to='up_data', verbose_name='数据附件1'),
        ),
        migrations.AlterField(
            model_name='datalist',
            name='data_file2',
            field=models.FileField(blank=True, null=True, upload_to='up_data', verbose_name='数据附件2'),
        ),
        migrations.AlterField(
            model_name='datalist',
            name='data_file3',
            field=models.FileField(blank=True, null=True, upload_to='up_data', verbose_name='数据附件3'),
        ),
        migrations.AlterField(
            model_name='userapply',
            name='result',
            field=models.CharField(blank=True, choices=[('未审核', '未审核'), ('审核中', '审核中'), ('审核通过', '审核通过'), ('审核未通过', '审核未通过')], default='未审核', max_length=10, null=True, verbose_name='申请结果'),
        ),
    ]
