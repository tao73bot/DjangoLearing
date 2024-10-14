from django.db import models
from django.utils import timezone

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
