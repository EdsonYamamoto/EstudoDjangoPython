from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from machineLearning.machineLearning import MachineLearning
import pdb
def teste(request):
    print('teste')

    return render(request, 'teste.html',{'form':'asdasd'})


def testePost(request):
    dadoPego = request.POST['dadoString']
    print(dadoPego)

    #if(request.method is "post"):
    #pdb.set_trace()

    mach = MachineLearning.Main(object)

    #return render(request, 'teste.html',{'form':'asdasd'})
    return HttpResponse(mach)