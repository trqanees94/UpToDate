# Generated by Django 2.0.3 on 2018-03-15 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reddit', '0007_user_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitter_post',
            name='icon',
            field=models.CharField(default='', max_length=200),
        ),
    ]
