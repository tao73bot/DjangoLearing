from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class TaoihdDetails(models.Model):
    TAOHID_TYPE_CHOICES = [
        ('ML', 'Maulana'),
        ('SH', 'Sheikh'),
        ('AL', 'Alim'),
        ('UL', 'Ulama'),
        ('MU', 'Mufassir'),
        ('MO', 'Moulan'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='taohid/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=TAOHID_TYPE_CHOICES, default='ML')
    description = models.TextField(default='')

    def __str__(self):
        return self.name


# One to Many Relationship
class TaohidReview(models.Model):
    taohid = models.ForeignKey(TaoihdDetails, on_delete=models.CASCADE,related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} review on {self.taohid.name}"


# Many to Many Relationship

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    taohid_details = models.ManyToManyField(TaoihdDetails, related_name='stores')

    def __str__(self):
        return self.name
    

# One to One Relationship
class TaohidContact(models.Model):
    taohid = models.OneToOneField(TaoihdDetails, on_delete=models.CASCADE, related_name='contact')
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return f"Contact of {self.taohid.name}"