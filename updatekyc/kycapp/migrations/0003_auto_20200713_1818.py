# Generated by Django 3.0.8 on 2020-07-13 12:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kycapp', '0002_auto_20200713_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attestedimages',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
