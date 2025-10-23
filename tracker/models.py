from django.db import models

class Location(models.Model):
    username = models.CharField(max_length=150)
    latitude = models.FloatField()
    longitude = models.FloatField()
    accuracy = models.FloatField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} @ {self.timestamp:%Y-%m-%d %H:%M:%S}"
