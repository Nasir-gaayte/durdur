from django.shortcuts import render, redirect
from .models import CardMolel
from .forms import CardForm

def home(request):
    cards = CardMolel.objects.all()
    return render(request,'core/home.html', {
        'cards':cards,
    })


def service(request):
    return render(request,'core/service.html')


def city(request):
    return render(request,'core/city.html')


def about(request):
    return render(request,'core/about.html')



def addCards(request):
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('home')
    form = CardForm()
    return render (request, 'core/add_card.html',{
        'form':form,
    })    
    
    
def cardDetail(request, pk):
    c =  CardMolel.objects.get(id=pk)
    return render(request,'core/card_detail.html',{
        'c':c,
    })   