# Generated by Django 3.1.6 on 2021-07-23 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('physician', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientWaitingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receptionist', models.BooleanField(default=False)),
                ('nurse', models.BooleanField(default=False)),
                ('triage', models.BooleanField(default=False)),
                ('physician', models.BooleanField(default=False)),
                ('radiologist', models.BooleanField(default=False)),
                ('lab_technician', models.BooleanField(default=False)),
                ('department', models.CharField(max_length=25)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='patient_waiting_list',
        ),
    ]
