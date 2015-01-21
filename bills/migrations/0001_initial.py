# encoding: utf8
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('front', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='expenses',
            fields=[
                ('purchase_order_no', models.IntegerField(max_length=3, serialize=False, primary_key=True)),
                ('rate_of_pure', models.IntegerField(max_length=15)),
                ('customer_id', models.ForeignKey(to='front.category', to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
