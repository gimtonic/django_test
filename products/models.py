from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=64,blank=True,null=True,default=None)
    price = models.DecimalField(max_digits=10,decimal_places=2, default=0)           #
    description=models.TextField(blank=True,null=True,default=None)
    #для картинок будет отдельная модель
    is_active=models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
#для картинок
class ProductImage(models.Model):
    product=models.ForeignKey(Product,blank=True,null=True,default=None)
    #куда можно загружить относитьно папки media
    image=models.ImageField(upload_to='products_images/')
    #отключаем товар из показа. по умолчанию активный тру.
    is_active=models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True,auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Фотографии'
        verbose_name_plural = 'Фотографии'