# Generated by Django 2.0.1 on 2019-08-30 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20190829_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_image'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
