from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

def sign_in(request):
    if request.method == 'POST':
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('')
        else:
            return render(request, 'signin.html', {'error_message':'Nieprawid³owy login lub has³o'})
    else:
        return render(request, 'signin.html')

def sign_out(request):
    logout(request)
    return redirect('')

def sign_up(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.groups.add(Group.objects.get(name = 'user'))
            return redirect('sign_in')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
