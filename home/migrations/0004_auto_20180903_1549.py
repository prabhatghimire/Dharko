# Generated by Django 2.1 on 2018-09-03 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180901_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='name',
            field=models.CharField(default=1, max_length=140),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='photo',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]