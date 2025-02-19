# Generated by Django 4.2 on 2025-02-10 15:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('employer', '0002_jobpost_remove_employerprofile_job_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/')),
                ('age', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('documents', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('applied_at', models.DateTimeField(auto_now_add=True)),
                ('job_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='employer.jobpost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
