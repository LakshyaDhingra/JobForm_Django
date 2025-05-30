from django.db import models

# Create your models here.


class Form(models.Model):
    objects = None
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)

    # Giving string representation of instance instead of python instance(gibberish)
    def __str__(self):
        return f"{self.first_name}{self.last_name}"

