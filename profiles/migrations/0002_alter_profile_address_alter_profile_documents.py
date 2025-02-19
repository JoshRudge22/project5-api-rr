# Generated by Django 4.2 on 2025-02-07 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='documents',
            field=models.FileField(blank=True, null=True, upload_to='documents/'),
        ),
    ]
