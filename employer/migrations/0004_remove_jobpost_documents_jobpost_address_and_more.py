# Generated by Django 4.2 on 2025-02-12 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employer', '0003_jobapplication'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobpost',
            name='documents',
        ),
        migrations.AddField(
            model_name='jobpost',
            name='address',
            field=models.CharField(default='No address provided', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='employer_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employer.employerprofile'),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='pay_rate',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='working_days',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='working_hours',
            field=models.CharField(max_length=100),
        ),
    ]
