# Generated by Django 2.1.3 on 2019-04-13 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0004_auto_20190413_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='response_time',
            field=models.IntegerField(default=0),
        ),
    ]