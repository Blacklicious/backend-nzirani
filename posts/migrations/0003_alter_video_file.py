# Generated by Django 4.2.5 on 2023-10-03 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_article_date_alter_article_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='video/publications/videos/'),
        ),
    ]
