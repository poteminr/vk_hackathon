# Generated by Django 2.2.5 on 2019-09-13 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='text',
            field=models.TextField(help_text='Enter text', max_length=1000),
        ),
    ]
