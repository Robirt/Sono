from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from .services.album_service import AlbumService
from .forms import SignUpForm

albumService: AlbumService = AlbumService();

def sign_in(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm(request)
    
    return render(request, 'app/sign_in.html', {'form': form, 'group': request.user.groups.first().name if request.user.groups.first() else None })

def sign_out(request):
    logout(request)
    return redirect('home')

def sign_up(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.groups.add(Group.objects.get(name='Users'))
            return redirect('sign_in')
    else:
        form = UserCreationForm()
    return render(request, 'app/sign_up.html', {'form': form, 'group': request.user.groups.first().name if request.user.groups.first() else None})

def home(request):
    return render(request, 'app/home.html', {'group': request.user.groups.first().name if request.user.groups.first() else None, 'username': request.user.username})

def catalog(request):
    albums = albumService.get_albums()
    return render(request, 'app/catalog.html', {'albums' : albums,'group': request.user.groups.first().name if request.user.groups.first() else None})

def about(request):
    return render(request, 'app/about.html', {'group': request.user.groups.first().name if request.user.groups.first() else None})

def contact(request):
    return render(request,'app/contact.html',{'group': request.user.groups.first().name if request.user.groups.first() else None})
