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
                ('rating', models.IntegerField(default=0, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Code',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CodeComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('code', models.ForeignKey(to='openapp.Code')),
            ],
            options={
                'verbose_name_plural': 'Code Comments',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='CodeFeedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('code', models.ForeignKey(to='openapp.Code')),
            ],
            options={
                'verbose_name_plural': 'Code Feedback',
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
                ('version', models.CharField(max_length=10, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('project', models.ForeignKey(to='openapp.Project')),
            ],
            options={
                'verbose_name_plural': 'Project Comments',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProjectFeedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('project', models.ForeignKey(to='openapp.Project')),
            ],
            options={
                'verbose_name_plural': 'Project Feedback',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=15, blank=True)),
                ('middle_name', models.CharField(max_length=20, blank=True)),
                ('last_name', models.CharField(max_length=25, blank=True)),
                ('username', models.CharField(unique=True, max_length=15)),
                ('password', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='projectfeedback',
            name='user',
            field=models.ForeignKey(to='openapp.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='projectcomment',
            name='user',
            field=models.ForeignKey(to='openapp.User'),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='language',
            unique_together=set([('name', 'version')]),
        ),
        migrations.AddField(
            model_name='codefeedback',
            name='user',
            field=models.ForeignKey(to='openapp.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='codecomment',
            name='user',
            field=models.ForeignKey(to='openapp.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='code',
            name='comments',
            field=models.ManyToManyField(related_name='code_comments', through='openapp.CodeComment', to='openapp.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='code',
            name='feedback',
            field=models.ManyToManyField(related_name='code_feedback', through='openapp.CodeFeedback', to='openapp.User'),
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
        migrations.RemoveField(
            model_name='project',
            name='desc',
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
            field=models.ManyToManyField(related_name='project_comments', through='openapp.ProjectComment', to='openapp.User'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='feedback',
            field=models.ManyToManyField(related_name='project_feedback', through='openapp.ProjectFeedback', to='openapp.User'),
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
            field=models.IntegerField(default=0),
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
        migrations.AlterField(
            model_name='project',
            name='source',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
