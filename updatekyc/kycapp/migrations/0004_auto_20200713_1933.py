# Generated by Django 3.0.8 on 2020-07-13 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kycapp', '0003_auto_20200713_1818'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='adhar_image1',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='adhar_image2',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='pancard',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
        migrations.DeleteModel(
            name='AttestedImages',
        ),
    ]
