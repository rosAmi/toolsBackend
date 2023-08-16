from django.db import models


class Tool(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name + ' - ' + self.description