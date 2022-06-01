from django.db import models

class Item(models.Model):
    title = models.CharField('nombre', max_length=255)
    price = models.DecimalField('Precio', max_digits=9, decimal_places=2)
    image = models.ImageField('Imagen', null=True, blank=True)

    def __str__(self):
        return self.title


class CartProduct(models.Model):
    item = models.ForeignKey(Item, verbose_name='Objeto',
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.item.title

class LikeProduct(models.Model):
    item = models.ForeignKey(Item, verbose_name='Objeto',
                             on_delete=models.CASCADE)

    def __str__(self):
        return self.item.title
