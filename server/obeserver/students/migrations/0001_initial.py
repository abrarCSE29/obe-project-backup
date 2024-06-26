# Generated by Django 5.0.6 on 2024-05-22 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(max_length=5, unique=True)),
                ('exam_roll', models.IntegerField(max_length=10, unique=True)),
                ('registration_no', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('batch', models.IntegerField(max_length=3)),
                ('phone_no', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
