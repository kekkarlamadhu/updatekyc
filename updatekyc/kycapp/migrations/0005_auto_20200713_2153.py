# Generated by Django 3.0.8 on 2020-07-13 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kycapp', '0004_auto_20200713_1933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='mobile_number',
            new_name='phone_number',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='adhar_image1',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='adhar_image2',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='district',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='middle_name',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='pancard',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='pin_code',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='state',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='default-avatar.png', null=True, upload_to='users/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]