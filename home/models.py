from django.db import models

# Create your models here.


class History(models.Model):

    location = models.CharField(max_length=500, null=True)
    area = models.FloatField()
    bedrooms = models.IntegerField()
    bathroom = models.IntegerField()
    estimated_price = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.location