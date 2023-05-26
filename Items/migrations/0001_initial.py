# Generated by Django 4.1.2 on 2023-05-25 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itemName', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('barcode_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('price', models.DecimalField(decimal_places=4, max_digits=19)),
                ('photo', models.ImageField(upload_to='Item')),
                ('inStock', models.IntegerField(default=0)),
            ],
        ),
    ]