# Generated by Django 2.1.7 on 2019-02-24 16:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_auto_20190224_1614'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Post2',
            new_name='Post',
        ),
    ]
