from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from accounts.forms import RegistrationForm
from django.contrib import messages
from accounts.models import UserProfile
from accounts.forms import ProfilUpdateForm,UserupdateForm
from tweeter.models import Tweet



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
    tweet=Tweet.objects.filter(user=request.user)
    prof=UserProfile.objects.get(user=request.user)
    userform=UserupdateForm(instance=request.user)
    profileform=ProfilUpdateForm(instance=prof)
    if request.method=='POST':
        userform=UserupdateForm(request.POST or None,request.FILES or None,instance=request.user)
        profileform=ProfilUpdateForm(request.POST or None,request.FILES or None,instance=prof)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()
            return HttpResponseRedirect('/')
    context={
    'prof':prof,
    'userform':userform,
    'profileform':profileform,
    'tweet':tweet
    }
    return render(request,'accounts/profile.html',context)
def followingView(request):
    followingObj=UserProfile.objects.filter(user=request.user)
    context={
    'followingObj':followingObj
    }
    return render(request,'accounts/following.html',context)
def followersView(request):
    followingObj=UserProfile.objects.filter(user=request.user)
    context={
    'followingObj':followingObj
    }
    return render(request,'accounts/followers.html',context)
