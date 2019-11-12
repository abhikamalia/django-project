# Generated by Django 2.1 on 2019-11-05 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('discount', models.FloatField()),
            ],
        ),
    ]
