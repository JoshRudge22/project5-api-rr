from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    documents = models.FileField(upload_to='documents/', null=True, blank=True)
    
    JOB_CHOICES = [
        ('bus_driver', 'Bus driver'),
        ('chauffeur', 'Chauffeur'),
        ('delivery_commerce', 'Delivery (commerce)'),
        ('emergency_medical_technician', 'Emergency medical technician (ambulance driver)'),
        ('motorman', 'Motorman (tram/streetcar driver)'),
        ('pay_driver', 'Pay driver'),
        ('racing_driver', 'Racing driver'),
        ('taxicab_driver', 'Taxicab driver'),
        ('test_driver', 'Test driver'),
        ('train_driver', 'Train driver'),
        ('truck_driver', 'Truck driver'),
        ('pilot', 'Pilot'),
        ('valet_parking', 'Valet Parking'),
        ('on_road_professional', 'On-road professional'),
        ('class1', 'Class 1'),
        ('class2', 'Class 2'),
        ('7_5_tonne', '7.5 tonne'),
    ]
    
    # Single preferred role instead of multiple job roles
    preferred_role = models.CharField(
        max_length=50,
        choices=JOB_CHOICES,
        null=True, blank=True
    )
    
    LOOKING_FOR_WORK_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
    ]
    looking_for_work = models.CharField(
        max_length=3,
        choices=LOOKING_FOR_WORK_CHOICES,
        default='no',
    )

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
