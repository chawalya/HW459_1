# Generated by Django 2.0.1 on 2018-02-22 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=15)),
                ('dob', models.DateField(blank=True, null=True)),
                ('credit_amount', models.DecimalField(decimal_places=2, max_digits=15)),
                ('memo', models.CharField(max_length=500)),
            ],
        ),
    ]
