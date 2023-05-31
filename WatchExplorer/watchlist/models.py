from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class WatchData(models.Model):
    title = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255, blank=True)
    price = models.CharField(max_length=100, blank=True)
    post_date = models.DateTimeField()
    source = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.title
