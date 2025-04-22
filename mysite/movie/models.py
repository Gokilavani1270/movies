from django.db import models

# Create your models here.
class MovieData(models.Model):
    def __str__(self):
        return self.name

    name=models.CharField(max_length=100)
    duration=models.FloatField()
    rating=models.FloatField()
    typ=models.CharField(max_length=10,default='action')
    image=models.ImageField(upload_to='Images/', default="Images/None/noimg.jpg")

    