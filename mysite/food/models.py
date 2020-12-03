from django.db import models

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image= models.CharField(max_length=500, default="https://lh3.googleusercontent.com/proxy/i6MxMUVrUmfPztimRyLkJe8Vf3_-oJdxnivTDGwJaG-k7rqV4xP6T00e6e_uvhBcHafpQKBiP7XhhE6BOICZXPVZdftMEcijVOKVGO7PljydnzuoaRyWIYFV5Ncb")

