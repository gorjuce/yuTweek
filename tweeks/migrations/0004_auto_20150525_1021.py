# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tweeks', '0003_auto_20150525_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweek',
            name='author',
            field=models.ForeignKey(related_name=b'author', to=settings.AUTH_USER_MODEL),
        ),
    ]
