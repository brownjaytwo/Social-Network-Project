# Generated by Django 2.0 on 2020-01-30 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_photopost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photopost',
            name='user',
        ),
        migrations.RemoveField(
            model_name='post',
            name='user',
        ),
        migrations.DeleteModel(
            name='PhotoPost',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
