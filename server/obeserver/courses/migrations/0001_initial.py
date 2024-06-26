# Generated by Django 5.0.6 on 2024-05-21 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.CharField(blank=True, max_length=10, null=True)),
                ('course_name', models.CharField(blank=True, max_length=40, null=True)),
                ('exam_title', models.CharField(blank=True, max_length=60, null=True)),
                ('active_status', models.BooleanField(default=False)),
            ],
        ),
    ]
