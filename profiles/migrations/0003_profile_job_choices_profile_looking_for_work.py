# Generated by Django 4.2 on 2025-02-07 13:58

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_address_alter_profile_documents'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='job_choices',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('bus_driver', 'Bus driver'), ('chauffeur', 'Chauffeur'), ('delivery_commerce', 'Delivery (commerce)'), ('emergency_medical_technician', 'Emergency medical technician (ambulance driver)'), ('motorman', 'Motorman (tram/streetcar driver)'), ('pay_driver', 'Pay driver'), ('racing_driver', 'Racing driver'), ('taxicab_driver', 'Taxicab driver'), ('test_driver', 'Test driver'), ('train_driver', 'Train driver'), ('truck_driver', 'Truck driver'), ('pilot', 'Pilot'), ('valet_parking', 'Valet Parking'), ('on_road_professional', 'On-road professional'), ('class1', 'Class 1'), ('class2', 'Class 2'), ('7_5_tonne', '7.5 tonne')], max_length=219, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='looking_for_work',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], default='no', max_length=3),
        ),
    ]
