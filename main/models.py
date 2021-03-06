from django.db import models

# Create your models here.


class ExtraInfo(models.Model):
    RODZAJE = {
        (0, 'Nieznany'),
        (1, 'Horror'),
        (2, 'Komedia'),
        (3, 'Sci-Fi'),
        (4, 'Drama')
    }
    czas_trwania = models.IntegerField(default=0)
    rodzaj = models.IntegerField(default=0, choices=RODZAJE)


class Aktor(models.Model):
    imie = models.CharField(max_length=128)
    nazwisko = models.CharField(max_length=128)
    # filmy = models.ManyToManyField(Movie)

    def __str__(self):
        return '{} {}'.format(self.imie, self.nazwisko)


class Movie(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(default='')
    year = models.IntegerField(null=True, blank=True)
    released = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(null=True, blank=True, decimal_places=7, max_digits=10)
    photo = models.ImageField(null=True, blank=True, upload_to='plakaty')
    # info = models.OneToOneField(ExtraInfo, on_delete=models.CASCADE)
    # info = models.ForeignKey(ExtraInfo, on_delete=models.CASCADE, unique=True)
    actors = models.ManyToManyField(Aktor)

    def __str__(self):
        return self.name_with_year()

    def name_with_year(self):
        return self.name + ' ({})'.format(self.year)


class Review(models.Model):
    text = models.CharField(default='', blank=True, max_length=128)
    starts = models.IntegerField(default=5)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)





