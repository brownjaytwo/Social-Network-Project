# Generated by Django 2.0.4 on 2019-08-29 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190828_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='socialnetwork/media/profile_image/woody.png', upload_to='profile_image'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.IntegerField(default=''),
        ),
    ]