# Generated by Django 3.2.5 on 2021-07-23 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('physician', '0002_auto_20210723_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientwaitinglist',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
