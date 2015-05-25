# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweeks', '0002_tweek_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweek',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='tweek',
            name='author',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
