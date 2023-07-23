from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

#Country - For nationality search
class Country(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name
    
# Tag system
class TagType(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']

class Tag(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField()
    type = models.ForeignKey(TagType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['type', 'name']

# Person - People involved in the creation of horror media
class Person(models.Model):
    fname = models.CharField(max_length=30, null=True)
    lname = models.CharField(max_length=30, null=True)
    nickname = models.CharField(max_length=30, null=True)
    bday = models.DateField(null=True)
    dday = models.DateField(null=True)

    def __str__(self):
        return self.nickname if self.lname is None else self.namefname + " " + self.lname

class Group(models.Model):
    name = models.CharField(max_length=100)

    # Dates
    creationdate = models.DateField(null=True, blank=True)
    defunctdate = models.DateField(null=True, blank=True)

    country = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Entry (models.Model):
    title = models.CharField(max_length=120, null=False)
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag)

""" # Game specific models
class Game(Entry):
    releasedate = models.DateField()

    #Developers
    devGroups = models.ManyToManyField(Group, related_name="devGroups")
    devPeople = models.ManyToManyField(Person)

    publishers = models.ManyToManyField(Group, related_name="publishers")

    platforms = models.ManyToManyField('Platform')
    engine = models.ForeignKey('Engine', on_delete=models.SET_NULL, null=True, blank=True, related_name="engine")

 

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

class Webseries(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)

    # Dates
    startdate = models.DateField()
    enddate = models.DateField()

    creators = models.ManyToManyField(Person)

    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title """