from django.db import models

class WatchData(models.Model):
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    post_date = models.DateTimeField()
    source = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    class Meta:
        verbose_name_plural = "Watch Data"
    def __str__(self):
        return self.title
