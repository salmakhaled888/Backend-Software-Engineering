from django.db import models

from django.db import models


# Create your models here.
class Item(models.Model):
    itemName = models.CharField(max_length=100)  # column
    description = models.TextField(max_length=1000)
    barcode_id = models.IntegerField(primary_key=True , default=0)
    price = models.DecimalField(max_digits=19, decimal_places=4)
    photo = models.ImageField(upload_to='Item')
    inStock = models.IntegerField(default=0)


    def _str_(self):
        return self.itemName
