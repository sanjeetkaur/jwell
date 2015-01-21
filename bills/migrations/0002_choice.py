# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bills', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.ForeignKey(to_field=b'purchase_order_no', blank=True, to='bills.expenses', null=True)),
                ('carat', models.IntegerField(max_length=2)),
                ('item', models.CharField(max_length=25)),
                ('weight', models.FloatField(max_length=10)),
                ('labour_cost', models.IntegerField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
