# Generated by Django 3.0.8 on 2020-10-19 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cfc_app', '0002_auto_20201018_0322'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='legiscan_id',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
