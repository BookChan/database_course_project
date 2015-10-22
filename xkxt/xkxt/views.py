from django.http import HttpResponse

from django.shortcuts import render



def login_handler(request):
    if request.method == 'POST':

        return HttpResponse(str(request.POST["password"]))
    return render(request,"login.html",{})

