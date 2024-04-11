# Generated by Django 5.0.4 on 2024-04-10 21:03

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Имя')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Автор статьи',
                'verbose_name_plural': 'Авторы статьи',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Категория')),
                ('description', models.TextField(verbose_name='Описание')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('tagline', models.CharField(default='', max_length=100, verbose_name='Подзоголовок')),
                ('description', models.TextField(verbose_name='Текст статьи')),
                ('poster', models.ImageField(upload_to='news/', verbose_name='Главная фотография')),
                ('country', models.CharField(max_length=30, verbose_name='Страна')),
                ('article_date', models.DateField(default=datetime.date.today, verbose_name='Дата выхода статьи')),
                ('url', models.SlugField(max_length=130, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
                ('author', models.ManyToManyField(related_name='new_author', to='news.author', verbose_name='Автор статьи')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Фильм',
                'verbose_name_plural': 'Фильмы',
            },
        ),
        migrations.CreateModel(
            name='AdditionalImg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='article_shots/', verbose_name='Изображение')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.new', verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Фото к статье',
                'verbose_name_plural': 'Фото к статье',
            },
        ),
    ]
