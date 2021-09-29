from django.db import models

class Person(models.Model):
    # Gender
    GENDER_CHOICES = [
        ('?', 'Inconnu'),
        ('M', 'Homme'),
        ('F', 'Femme'),
        ('O', 'Autre'),
    ]

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    nickname = models.CharField(max_length=100)

    date_of_birth = models.DateField(null=True, blank=True)

    date_of_death = models.DateField(null=True, blank=True)

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='?',
    )

    country = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return '{0}, {1}'.format(self.first_name, self.last_name)

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

class Tag(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name
