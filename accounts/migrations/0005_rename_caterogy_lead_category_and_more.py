# Generated by Django 4.2.5 on 2023-10-15 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_lead_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='caterogy',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='lead',
            old_name='subjet',
            new_name='subject',
        ),
    ]
