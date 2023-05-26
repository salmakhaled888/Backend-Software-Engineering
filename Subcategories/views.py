from rest_framework import viewsets
from Subcategories.Serializer import subCategoriesSerializer
from Subcategories.models import subCategories


class subCategoriesViewSet(viewsets.ModelViewSet):
    queryset = subCategories.objects.all()
    serializer_class = subCategoriesSerializer
