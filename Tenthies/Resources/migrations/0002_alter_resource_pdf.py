# Generated by Django 3.2.8 on 2021-12-15 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='pdf',
            field=models.FileField(upload_to='pdfs/% Y/% m/% d/'),
        ),
    ]