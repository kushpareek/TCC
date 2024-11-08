from django.db import models

# Create your models here.
# dashboard/models.py

from django.db import models
from django.contrib.auth.models import User

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
