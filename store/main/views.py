from django.contrib.auth import login
from django.db.models import Q
from django.shortcuts import render, redirect
from item.models import Item, Category

from .forms import SignUpForm

# Create your views here.

def index(request):
    item = Item.objects.order_by('-created_at')[:3]
    instagram = ''
    return render(request, 'main/index.html', {'item' : item, 'instagram':instagram})
def catalog(request):
    item = Item.objects.order_by('name')
    category = Category.objects.all()


    active_category = request.GET.get('y', '')

    if active_category:
        item = item.filter(category__slug=active_category)

    query = request.GET.get('query', '')

    if query:
        #item = item.filter(name_icontains=query)
        item = item.filter(Q(name__icontains = query) | Q(description__icontains=query))

    variables = {
        'item': item,
        'category': category,
        'active_category': active_category,
    }

    return render(request, 'main/catalog.html', variables)

def signup(request):
    if request.method == 'POST':
        f = SignUpForm(request.POST)

        if f.is_valid():
            user= f.save()

            login(request, user)

            return redirect('/')
    else:
        f = SignUpForm()

    return render(request, 'main/signup.html', {'f':f})

def login_old(request):
    return render(request, 'main/login.html')
