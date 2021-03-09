from django.db import models
from datetime import datetime
# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 100)
    disription = models.CharField(max_length = 500)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank = True)
    date = models.DateTimeField(default=datetime.now(),blank=True)


    def __str__(self):
        return self.title
