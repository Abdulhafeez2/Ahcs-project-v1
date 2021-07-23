# Generated by Django 3.2.5 on 2021-07-23 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20210723_2141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_Hospital_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_Lab_technician',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_Nurse',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_Patient',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_Pharmacist',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_Pharmacy_admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_Physician',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_Radiologist',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_Receptionist',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='Hospital_admin', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
