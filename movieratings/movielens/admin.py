from django.contrib import admin
from .models import Movie, Rater, Ratings

admin.site.register(Movie)
admin.site.register(Rater)
admin.site.register(Ratings)

# Register your models here.
