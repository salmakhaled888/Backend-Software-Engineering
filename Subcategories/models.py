from django.db import models

from Categories.models import Categories


class subCategories(models.Model):
    subCategories_name = models.CharField(max_length=500)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE,max_length=500)
    def _str_(self):
        return self.subCategories_name