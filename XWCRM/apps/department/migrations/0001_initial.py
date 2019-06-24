# Generated by Django 2.1.7 on 2019-06-24 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='部门名称')),
                ('desc', models.TextField(blank=True, max_length=256, null=True, verbose_name='部门描述')),
                ('is_delete', models.BooleanField(default=False, verbose_name='逻辑删除')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '部门表',
                'verbose_name_plural': '部门表',
                'db_table': 'deparment',
            },
        ),
    ]