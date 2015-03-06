# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookmarks1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('parent', models.IntegerField(null=True)),
                ('bid', models.IntegerField()),
                ('fk', models.IntegerField()),
                ('title', models.CharField(max_length=250, blank=True)),
                ('position', models.IntegerField()),
                ('url', models.URLField(max_length=250, blank=True)),
                ('description', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='citys1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city_name', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': '\u57ce\u5e02',
                'verbose_name_plural': '\u57ce\u5e02',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=250, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('content', models.CharField(default=b'', max_length=250, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'ordering': ('-create_time',),
                'verbose_name': '\u7b14\u8bb0',
                'verbose_name_plural': '\u7b14\u8bb0',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='sale_orders1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('month', models.CharField(default=b'', max_length=250, choices=[(b'January', '\u4e00\u6708'), (b'February', '\u4e8c\u6708'), (b'March', '\u4e09\u6708'), (b'April', '\u56db\u6708'), (b'May', '\u4e94\u6708'), (b'June', '\u516d\u6708'), (b'July', '\u4e03\u6708'), (b'August', '\u516b\u6708'), (b'September', '\u4e5d\u6708'), (b'October', '\u5341\u6708'), (b'November', '\u5341\u4e00\u6708'), (b'December', '\u5341\u4e8c\u6708')])),
                ('value', models.IntegerField()),
                ('city', models.ForeignKey(related_name='cityID', verbose_name=b'\xe5\x9f\x8e\xe5\xb8\x82', to='bm1.citys1')),
            ],
            options={
                'verbose_name': '\u9500\u552e\u8ba2\u5355',
                'verbose_name_plural': '\u9500\u552e\u8ba2\u5355',
            },
            bases=(models.Model,),
        ),
    ]
