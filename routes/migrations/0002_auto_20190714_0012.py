# Generated by Django 2.2.3 on 2019-07-13 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gym2',
            name='key',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
