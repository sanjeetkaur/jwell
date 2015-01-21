# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(null=True)),
                ('metal', models.CharField(max_length=10)),
                ('mode_of_payment', models.CharField(max_length=15)),
                ('telephone', models.IntegerField(max_length=10)),
                ('address', models.CharField(max_length=75)),
                ('customer_id', models.IntegerField(max_length=4)),
            ],
            options={
                'verbose_name_plural': b'Categories',
            },
            bases=(models.Model,),
        ),
    ]
