from django.db import models


class Rater(models.Model):
    user_id = models.IntegerField(primary_key=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=2)
    occupation = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=10)


class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=200)


class Ratings(models.Model):
    rater = models.ForeignKey(Rater, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.IntegerField()
