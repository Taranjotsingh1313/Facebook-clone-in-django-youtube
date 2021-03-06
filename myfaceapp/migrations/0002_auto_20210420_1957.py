# Generated by Django 3.1.7 on 2021-04-20 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myfaceapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='profileuser',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='myfaceapp.profilemodel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
