# Generated by Django 2.0.1 on 2019-08-30 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20190830_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='socialnetwork/media/profile_image/default.png', upload_to='profile_image'),
        ),
    ]
