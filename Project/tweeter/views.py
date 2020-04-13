from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from tweeter.models import Tweet
from tweeter.forms import TweetCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator

@login_required
def Home(request):
    tweet=Tweet.objects.all().order_by('-timestamp','-updated')
    query=request.GET.get('q',None)
    if query is not None:
        tweet=tweet.filter(Q(content__icontains=query)|Q(user__username__icontains=query))
    if request.method=="POST":
        form=TweetCreationForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            create=form.save(commit=False)
            create.user=request.user
            create.save()
            form=TweetCreationForm()
            return HttpResponseRedirect('/')
    else:
        form=TweetCreationForm()
    context={
    'tweet':tweet,
    'form':form
    }
    return render(request,'tweeter/home.html',context)
'''def search(request,*args,**kwargs):

    #pages=Paginator(request,results,1)
    context={
    #'items':pages[0],
    #'page_range':pages[1],
    'results':results
    }
    return render(request,'tweeter/search.html',qs)'''
@login_required
def TweetDetails(request,id):
    tweetdetails=Tweet.objects.get(id=id)
    context={
    'tweetdetails':tweetdetails
    }
    return render(request,'tweeter/details.html',context)
@login_required
def CreatTweetView(request):

    context={
    }
    return render(request,'tweeter/create.html',context)
@login_required
def UpdateView(request,id):
    if request.user.is_authenticated:
        tweetobj=Tweet.objects.get(id=id,user=request.user)
        form=TweetCreationForm(instance=tweetobj)
        if request.method=="POST":
            form=TweetCreationForm(request.POST or None,request.FILES or None,instance=tweetobj)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/')
    context={
    'form':form
    }
    return render(request,'tweeter/update.html',context)
@login_required
def deleteView(request,id):
    if request.user.is_authenticated:
        deleteTweet=Tweet.objects.get(id=id,user=request.user)
        deleteTweet.delete()
    return HttpResponseRedirect('/')
