# Generated by Django 3.0.8 on 2020-07-14 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kycapp', '0005_auto_20200713_2153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='bio',
            new_name='address',
        ),
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
            name='city',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='profile',
            name='company_name',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='profile',
            name='district',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='profile',
            name='middle_name',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='profile',
            name='pancard',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='profile',
            name='pancard_image',
            field=models.ImageField(blank=True, null=True, upload_to='users/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='pincode',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
