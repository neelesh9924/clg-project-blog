# Generated by Django 3.1 on 2020-10-16 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0006_auto_20201016_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='click aboove to read blog post..', max_length=25),
        ),
    ]
