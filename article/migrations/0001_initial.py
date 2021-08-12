# Generated by Django 3.1.7 on 2021-08-06 07:15

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='テキスト')),
                ('title', models.TextField(max_length=50, verbose_name='タイトル')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
            ],
            options={
                'verbose_name': '記事',
                'verbose_name_plural': '記事',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.TextField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='コメント日時')),
                ('good', models.IntegerField(default=0, verbose_name='いいねの数')),
                ('comment_to', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comment_to', to='article.article')),
            ],
            options={
                'verbose_name': 'コメント',
                'verbose_name_plural': 'コメント',
            },
        ),
    ]
