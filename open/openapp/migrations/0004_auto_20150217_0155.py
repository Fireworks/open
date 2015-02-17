# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openapp', '0003_auto_20150210_0159'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('code', models.ForeignKey(to='openapp.Project')),
                ('user', models.ForeignKey(to='openapp.User')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FeedbackProject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('code', models.ForeignKey(to='openapp.Project')),
                ('user', models.ForeignKey(to='openapp.User')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='project',
            old_name='desc',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='project',
            name='lang',
        ),
        migrations.RemoveField(
            model_name='project',
            name='owner',
        ),
        migrations.AddField(
            model_name='project',
            name='comments',
            field=models.ManyToManyField(related_name='project_comments', through='openapp.CommentProject', to='openapp.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='feedback',
            field=models.ManyToManyField(related_name='project_feedback', through='openapp.FeedbackProject', to='openapp.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='language',
            field=models.ForeignKey(to='openapp.Language', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(related_name='project_users', to='openapp.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='name',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
    ]
