# Generated by Django 2.0.2 on 2018-04-03 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('intro', models.TextField(blank=True, null=True)),
                ('dynasty', models.CharField(blank=True, max_length=10, null=True)),
                ('weight', models.IntegerField()),
            ],
            options={
                'db_table': 'poetry_author',
            },
        ),
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('dynasty', models.CharField(default='S', max_length=10)),
                ('author_name', models.CharField(max_length=150)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poem.Author')),
            ],
            options={
                'db_table': 'poems',
            },
        ),
        migrations.CreateModel(
            name='Poetry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('dynasty', models.CharField(max_length=10)),
                ('author_name', models.CharField(max_length=150)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poetries', to='poem.Author')),
            ],
            options={
                'db_table': 'poetry',
            },
        ),
        migrations.CreateModel(
            name='PoetryAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('intro', models.TextField(blank=True, null=True)),
                ('dynasty', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'db_table': 'poetry_author_bak',
            },
        ),
    ]
