from django.db import models
class Movies_data(models.Model):
    movie_id=models.IntegerField(unique=True)
    movie_name=models.CharField(max_length=100)
    timings=models.TimeField(max_length=100)
    location=models.CharField(max_length=100)
