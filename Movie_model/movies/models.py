from django.db import models

class Moviedata(models.Model):

    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    movie_type = models.CharField(max_length=200, default='action')
    image = models.ImageField(upload_to='Images/', default='Images/None/Noimg.jpg')
