# Generated by Django 2.0.1 on 2018-02-22 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0002_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rent',
            name='return_datetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='rent',
            name='start_datetime',
            field=models.DateTimeField(null=True),
        ),
    ]