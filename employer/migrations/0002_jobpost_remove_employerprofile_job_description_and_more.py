# Generated by Django 4.2 on 2025-02-10 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('pay_rate', models.CharField(max_length=255)),
                ('working_days', models.CharField(max_length=255)),
                ('working_hours', models.CharField(max_length=255)),
                ('documents', models.FileField(blank=True, null=True, upload_to='job_documents/')),
            ],
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='job_description',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='pay_rate',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='working_days',
        ),
        migrations.RemoveField(
            model_name='employerprofile',
            name='working_hours',
        ),
        migrations.AlterField(
            model_name='employerprofile',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='company_logos/'),
        ),
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.AddField(
            model_name='jobpost',
            name='employer_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_posts', to='employer.employerprofile'),
        ),
    ]
