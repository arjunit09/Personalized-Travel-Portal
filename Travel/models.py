from django.db import models
from django.contrib.auth.models import User
class Destination(models.Model):
    Name=models.TextField()
    budget=models.DecimalField(max_digits=8, decimal_places=2)
    Duration=models.TextField()
    Season=models.TextField()
    activate=models.TextField()
    def __str__(self):
        return self.Name
class save_destination(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    destination=models.ForeignKey(Destination, on_delete=models.CASCADE)
        