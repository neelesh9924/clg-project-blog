# Generated by Django 3.1 on 2020-10-16 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0010_auto_20201016_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='website_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
