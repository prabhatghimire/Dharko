# Generated by Django 2.0.1 on 2018-02-27 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('date', models.DateTimeField()),
                ('detail', models.CharField(max_length=140)),
                ('body', models.FileField(upload_to='')),
            ],
        ),
    ]