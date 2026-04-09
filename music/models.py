from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    genre = models.CharField(max_length=50)

    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.artist.name}"