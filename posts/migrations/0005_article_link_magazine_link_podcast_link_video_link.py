# Generated by Django 4.2.5 on 2023-10-12 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_article_creation_article_rubrique_magazine_creation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='YouTube Video Link'),
        ),
        migrations.AddField(
            model_name='magazine',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='YouTube Video Link'),
        ),
        migrations.AddField(
            model_name='podcast',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='YouTube Video Link'),
        ),
        migrations.AddField(
            model_name='video',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='YouTube Video Link'),
        ),
    ]
