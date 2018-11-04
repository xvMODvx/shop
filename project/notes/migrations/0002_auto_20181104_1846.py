# Generated by Django 2.1.3 on 2018-11-04 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='notes',
            field=models.TextField(default='Notes'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='notes',
            name='text',
            field=models.TextField(default='Text'),
        ),
    ]
