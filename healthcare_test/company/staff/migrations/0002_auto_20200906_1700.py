# Generated by Django 3.1.1 on 2020-09-06 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='department',
            options={'ordering': ['-dname']},
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ['-ename']},
        ),
    ]