from django.db import models

class Director(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    duration = models.TimeField()
    director = models.ForeignKey(
        Director,
        on_delete=models.CASCADE,
        related_name='movies'
    )

    def __str__(self):
        return self.title

class Review(models.Model):
    text = models.CharField(max_length=50)
    stars = models.IntegerField(default=1)
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    def __str__(self):
        return f"{self.text} ({self.stars} stars)"

