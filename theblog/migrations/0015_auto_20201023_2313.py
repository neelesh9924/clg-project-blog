# Generated by Django 3.1 on 2020-10-23 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0014_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='snippet',
            field=models.CharField(max_length=50),
        ),
    ]
