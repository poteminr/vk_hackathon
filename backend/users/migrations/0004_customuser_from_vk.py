# Generated by Django 2.2.5 on 2019-09-14 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190913_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='from_vk',
            field=models.BooleanField(default=True),
        ),
    ]
