# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
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
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
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
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
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
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('source', models.URLField()),
                ('rating', models.IntegerField(default=0, blank=True)),
                ('language', models.ForeignKey(to='openapp.Language', null=True)),
                ('users', models.ManyToManyField(related_name='project_users', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
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
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
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
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Project Feedback',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='language',
            unique_together=set([('name', 'version')]),
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
            field=models.ManyToManyField(related_name='code_users', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
