# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-08-02 13:26
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import django.utils.timezone
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_productfile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='productfile',
            name='filepath',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productfile',
            name='file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/home/rishav/Desktop/eCommerce-master/static_cdn/protected_media'), upload_to=products.models.upload_product_file_loc),
        ),
    ]
