# Generated by Django 2.1.3 on 2018-11-04 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20181104_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='category',
            field=models.CharField(default='New', max_length=50),
        ),
    ]