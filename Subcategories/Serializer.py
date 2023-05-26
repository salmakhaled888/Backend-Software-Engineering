from rest_framework import serializers
from Subcategories.models import subCategories


class subCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = subCategories
        fields = ['id','subCategories_name','category']