from django.shortcuts import render

def home(request):
    return render(
        request,
        'app/home.html'
        )

def signin(request):
    return render(
        request,
        'app/signin.html'
        )

def signup(request):
    return render(
        request,
        'app/signup.html'
        )

def catalog(request):
    return render(
        request,
        'app/catalog.html'
        )

def about(request):
    return render(
        request,
        'app/about.html'
        )
def contact(request):
    return render(
        request,
        'app/contact.html'
        )
