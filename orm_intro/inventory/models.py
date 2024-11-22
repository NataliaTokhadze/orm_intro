from django.db import models

class Table(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    stock = models.IntegerField()

    def __str__(self):
        return f'{self.name}, {self.description}, {self.price}, {self.stock}'