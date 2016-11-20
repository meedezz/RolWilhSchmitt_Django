from django.db import models
from app.forms import FormattedDateField

#Bilder
class R_Bild(models.Model):
    img = models.TextField(max_length=500)
    caption = models.TextField(max_length=500, blank=True) 
    date = FormattedDateField(blank=True)

    def __str__(self):
            return self.header

#Bücher
class R_Buch(models.Model):
    title = models.TextField(max_length=500)
    src = models.TextField(max_length=500)
    img = models.TextField(max_length=500) 

    def __str__(self):
            return self.header

#Objekte
class R_Objekt(models.Model):
    img = models.TextField(max_length=500)
    caption = models.TextField(max_length=500, blank = True)    
    date = FormattedDateField(blank=True)

    def __str__(self):
            return self.header

#Projekte
class R_Projekt(models.Model):
    img = models.TextField(max_length=500)   
    name = models.TextField(max_length=500)    
    def __str__(self):
            return self.header

class R_Projektbild(models.Model):
    img = models.TextField(max_length=500) 
    caption = models.TextField(max_length=500, blank=True)    
    date = FormattedDateField(blank=True)

    projekt_f = models.ForeignKey(R_Projekt, on_delete=models.CASCADE)

    def __str__(self):
            return self.header
