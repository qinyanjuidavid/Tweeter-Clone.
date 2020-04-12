from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from accounts.forms import RegistrationForm
from django.contrib import messages
from accounts.models import UserProfile



def Registration(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST or None,request.FILES or None)
        if form.is_valid:
            form.save()
            messages.success(request,'Your account has successfully was successfully created')
            return HttpResponseRedirect('/accounts/login/')
    else:
        form=RegistrationForm()
    context={
    'formreg':form
    }
    return render(request,'accounts/registration.html',context)
def ProfileView(request):
    context={

    }
    return render(request,'accounts/profile.html',context)
