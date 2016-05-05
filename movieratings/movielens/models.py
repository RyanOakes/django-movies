from django.db import models


class Movie(models.Model):
    movie_id = models.IntegerField()
    title = models.CharField(max_length=200)


class Rater(models.Model):
    ratings = models.ForeignKey(Ratings, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=1)
    occupation = models.CharField(max_length=20)
    zip_code = models.IntegerField(dfault=0)


class Ratings(models.Model):
    rater = models.ForeignKey(Rater, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    movie_id = models.IntegerField()
    rating = models.IntegerField()
