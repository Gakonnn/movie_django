from django.db import models


class Genr(models.Model):
    genr = models.CharField(max_length=30)
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.genr
class Movie(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200)
    year = models.IntegerField(max_length=4)
    during = models.IntegerField(max_length=10)
    grade = models.IntegerField(max_length=2)
    description = models.TextField()
    category = models.ForeignKey(to=Genr, on_delete=models.PROTECT)

    class Meta():
        ordering = ('id',)

    def __str__(self):
        return self.name

# Create your models here.
