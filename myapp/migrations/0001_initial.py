# Generated by Django 3.2.8 on 2021-10-09 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=50)),
                ('employee_age', models.IntegerField(default=0)),
                ('employee_contact', models.IntegerField(default=0)),
                ('employee_email', models.EmailField(max_length=50)),
            ],
        ),
    ]