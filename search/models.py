from django.db import models

class Film(models.Model):
    title = models.CharField(max_length = 200)
    location = models.CharField(max_length = 200)
    latitude = models.CharField(max_length = 200)
    longitude = models.CharField(max_length = 200)

    def __str__(self):
        return '%s %s %s %s' %(self.title, self.location, self.latitude, self.longitude)
