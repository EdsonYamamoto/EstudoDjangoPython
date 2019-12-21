from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

def teste(request):
    print('teste')

    return render(request, 'teste.html',{'form':'asdasd'})


def testePost(request):
    if request.method == 'POST':
        print("realmente eh um post")

    return render(request, 'teste.html',{'form':'asdasd'})