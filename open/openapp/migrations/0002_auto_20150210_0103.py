# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('source', models.TextField()),
                ('rating', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CommentCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('code', models.ForeignKey(to='openapp.Code')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FeedbackCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('code', models.ForeignKey(to='openapp.Code')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20)),
                ('version', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=15)),
                ('middle_name', models.CharField(max_length=20, null=True)),
                ('last_name', models.CharField(max_length=25)),
                ('username', models.CharField(unique=True, max_length=15)),
                ('password', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='language',
            unique_together=set([('name', 'version')]),
        ),
        migrations.AddField(
            model_name='feedbackcode',
            name='user',
            field=models.ForeignKey(to='openapp.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='commentcode',
            name='user',
            field=models.ForeignKey(to='openapp.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='code',
            name='comments',
            field=models.ManyToManyField(related_name='code_comments', through='openapp.CommentCode', to='openapp.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='code',
            name='feedback',
            field=models.ManyToManyField(related_name='code_feedback', through='openapp.FeedbackCode', to='openapp.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='code',
            name='language',
            field=models.ForeignKey(to='openapp.Language'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='code',
            name='users',
            field=models.ManyToManyField(related_name='code_users', to='openapp.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='desc',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='lang',
            field=models.CharField(max_length=25, choices=[(b'Python', b'Python'), (b'Javascript', b'Javascript'), (b'Java', b'Java')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='source',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
