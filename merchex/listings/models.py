from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Band(models.Model):
    
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
        
    name = models.fields.CharField(max_length = 100)
    genre = models.fields.CharField(choices = Genre.choices, max_length= 5,)
    biography = models.fields.CharField(max_length= 1000)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    active = models.fields.BooleanField( default= True)
    official_homepage = models.fields.URLField(null= True, blank= True)
    
    
    
    def __str__(self):
        return f'{self.name}'
    
class Listing(models.Model):
    
    class Type(models.TextChoices):
        Records = 'Re'
        Clothing = 'Cl'
        Posters = 'Po'
        Miscellaneous = 'Mi'
        
    title = models.fields.CharField(max_length= 100)
    description=models.fields.CharField(max_length= 1000)
    sold = models.BooleanField(default=False)
    year = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=4, choices = Type.choices)
    
    def __str__(self):
        return f'{self.title}'
    
    band = models.ForeignKey(Band, null = True, on_delete=models.SET_NULL)
    
    