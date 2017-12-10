from django.contrib import admin
from .models import *

#2 поля отображение
class SubscriberAdmin (admin.ModelAdmin):
#какие поля отоброжать
#    list_display = ["name","email"]
# если много полей то так
# Subscriber._meta.fields находит все поля из модели Subscriber
#field.name for field in - находит имя в каждом поле
# появится ещё колонка id
    list_display = [field.name for field in Subscriber._meta.fields]
#добавим фильтр
    list_filter = ["name"]
#input поиска
    search_fields = ["name","email"]
#при входе в саму запись можно не отоброжать поле email например
#    exclude = ["email"]
#при входе в саму запись можно показывать только поле email например
    fields = ["email"]
#можно добавить встроенную форму
#    inlines = [""]
#берёт данные из модели Subscriber
    class Meta:
        model = Subscriber

#просто регистрируем модель субскрайбер и новый класс SubscriberAdmin который переопределит настройки т.к. идёт 2-ым
admin.site.register(Subscriber, SubscriberAdmin)
