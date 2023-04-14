from django.db import models

class kitab(models.Model):
    Name = models.CharField(max_length=25)
    price = models.CharField(max_length=25)
    publisher = models.CharField(max_length=25)


    class Meta:
        db_table = "Book"

