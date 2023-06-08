from django.db import models


# Create your models here.

class Item(models.Model):
    item_name = models.CharField(max_length=200) # max_length is needed
    item_description = models.CharField(max_length=200)
    item_price = models.IntegerField()
    # since it is a link
    item_image = models.CharField(max_length=500, default="https://cdn.dribbble.com/users/1012566/screenshots/4187820/media/3cb974c28eb00627cc0671685c79ffd9.jpg")

    def __str__(self):
        return self.item_name   # allows database to return strings when Item.objects.all()
