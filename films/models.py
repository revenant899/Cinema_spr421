from django.db import models

class Film(models.Model):
    CATEGORY_CHOICES = [
        ('action', 'Action'),
        ('drama', 'Drama'),
        ('comedy', 'Comedy'),
        ('horror', 'Horror'),
        ('sci-fi', 'Sci-Fi'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='film_images/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    show_time = models.DateTimeField()

    def __str__(self):
        return self.name