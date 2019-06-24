# Generated by Django 2.1.7 on 2019-06-24 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_staffinfo_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffinfo',
            name='gender',
            field=models.BooleanField(choices=[(0, '女'), (1, '男')], default=1, verbose_name='性别'),
        ),
    ]