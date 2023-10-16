# Generated by Django 4.2.5 on 2023-10-15 22:57

import converter.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=converter.models.content_file_name)),
                ('title', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]