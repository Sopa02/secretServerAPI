from django.db import models

class Secret(models.Model):
    _hash = models.CharField(max_length=100)
    secretText = models.TextField()
    createdAt = models.DateTimeField()
    expiresAt = models.DateTimeField()
    remainingViews = models.IntegerField()

    def __str__(self):
        return self._hash