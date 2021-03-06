# Generated by Django 3.0.7 on 2020-06-10 07:07

import common.common
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('account', models.CharField(max_length=30, unique=True, verbose_name='账号')),
                ('email', models.CharField(max_length=50, unique=True, verbose_name='邮箱')),
                ('nick', models.CharField(max_length=20, unique=True, verbose_name='昵称')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='是否管理员')),
                ('is_staff', models.BooleanField(default=True, verbose_name='是否材料商帐号')),
                ('is_active', models.BooleanField(default=True, verbose_name='是否有效')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='注册时间')),
                ('update_time', models.DateTimeField(auto_now=True)),
                ('avatar', models.ImageField(blank=True, upload_to=common.common.get_file_path, verbose_name='头像')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '管理员帐号',
                'verbose_name_plural': '管理员帐号',
                'db_table': 'user',
            },
        ),
    ]
