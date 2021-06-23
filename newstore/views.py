from django.shortcuts import render


def newstore(request):
    return render(request, 'newstore/main.html')
