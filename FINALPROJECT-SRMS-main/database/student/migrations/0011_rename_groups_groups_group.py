# Generated by Django 3.2.5 on 2021-07-29 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_groups_class'),
    ]

    operations = [
        migrations.RenameField(
            model_name='groups',
            old_name='Groups',
            new_name='Group',
        ),
    ]
