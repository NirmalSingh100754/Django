from django.db import models
from django.utils import timezone


# Create your models here.
class ChaiVarity(models.Model):
    CHAI_TYPE_CHIOCE = [
        ("MC", "Masala Chai"),
        ("GC", "Ginger Chai"),
        ("TC", "Tulsi Chai"),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="chais/")
    date = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHIOCE)


    def __str__(self):
        return self.name
