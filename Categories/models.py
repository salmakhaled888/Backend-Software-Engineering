from django.db import models

class Categories (models.Model):
    category_name = models.CharField(max_length=500)
    def _str_(self):
        return self.category_name