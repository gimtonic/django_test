from django.shortcuts import render
from .forms import SubscriberForm

def landing(request):
    name = "Guest"
    form = SubscriberForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        #пишет в консоль
        print(request.POST)
        # cleaned_data -функция тоже что и выше кроме дополнительных полей.
        print(form.cleaned_data)
        #посмотреть имя
        data=form.cleaned_data
        print(data["name"])
        #если form=form.save() то форма пропадает
        new_form=form.save()
    return render(request,'landing/landing.html',locals())
