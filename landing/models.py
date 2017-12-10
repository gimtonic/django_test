from django.db import models

class Subscriber(models.Model):
    email=models.EmailField()
    name=models.CharField(max_length=128)

#любую запись в данной модели будет презентовать поле id
#self - запись из этой модели
    def __str__(self):
        return "Пользователь %s %s" % (self.name, self.email,)

    class Meta:
        verbose_name = 'MySubsciber'
        verbose_name_plural = 'MySubscibers'