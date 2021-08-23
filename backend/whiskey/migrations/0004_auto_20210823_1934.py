# Generated by Django 3.2.5 on 2021-08-23 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('whiskey', '0003_auto_20210823_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='brand',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='type', to='whiskey.type'),
        ),
        migrations.AddField(
            model_name='brand',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='region', to='whiskey.region'),
        ),
    ]
