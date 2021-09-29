from django.db import models
from common.models import Person, Group, Tag

class Game(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    releasedate = models.DateField()

    #Developers
    devGroups = models.ManyToManyField(Group, related_name="devGroups")
    devPeople = models.ManyToManyField(Person)

    publishers = models.ManyToManyField(Group, related_name="publishers")

    platforms = models.ManyToManyField('Platform')
    engine = models.ForeignKey('Engine', on_delete=models.SET_NULL, null=True, blank=True, related_name="engine")

    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Platform(models.Model):
    name = models.CharField(max_length=120)

    # Dates
    releasedate = models.DateField()
    discountdate = models.DateField(blank=True, null=True)

    platformtype = models.ForeignKey('PlatformType', on_delete=models.SET_NULL, null=True)
    manufacturers = models.ManyToManyField(Group)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class PlatformType(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(blank=True, null=True)
    generation = models.IntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Engine(models.Model):
    name = models.CharField(max_length=120)

    # Dates
    initreleasedate = models.DateField()
    lastreleasedate = models.DateField()

    # Relations with other engines
    predecessor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name="predecessor_id")
    successor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name="successor_id")

    # Developers
    devGroups = models.ManyToManyField(Group)
    devPeople = models.ManyToManyField(Person)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
