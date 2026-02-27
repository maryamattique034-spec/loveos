from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(request, "landing.html")

def welcome(request):
    return render(request, "welcome.html")

def game(request):
    return render(request, "game.html")

def special(request):
    return render(request, "special.html")

def letter(request):
    return render(request, "letter.html")

def final(request):
    return render(request, "final.html")
