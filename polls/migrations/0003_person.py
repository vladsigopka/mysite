# Generated by Django 4.1.1 on 2022-11-27 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_catalog_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=130)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('job_title', models.CharField(blank=True, max_length=30)),
                ('bio', models.TextField(blank=True)),
            ],
        ),
    ]
