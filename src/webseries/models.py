from django.db import models
from common.models import Person, Group, Tag

class Webseries(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)

    # Dates
    startdate = models.DateField()
    enddate = models.DateField()

    creators = models.ManyToManyField(Person)

    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
