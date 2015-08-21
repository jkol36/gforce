# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
        ('players', '0001_initial'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='players',
            field=models.ForeignKey(blank=True, to='players.Player', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='profile',
            name='teams',
            field=models.ForeignKey(blank=True, to='teams.Team', null=True),
            preserve_default=True,
        ),
    ]
