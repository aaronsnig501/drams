# Generated by Django 3.2.5 on 2021-09-08 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('whiskey', '0010_auto_20210831_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='whiskey',
            name='added_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='accounts.account'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='whiskey',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='whiskey',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]