from django.urls import path
from tweeter import views
app_name="tweeter"


urlpatterns=[
path('',views.Home,name="home"),
path('tweet/<id>/details/',views.TweetDetails,name="details"),
path('create/Post/',views.CreatTweetView,name="create"),
path('Post/Update/<id>/',views.UpdateView,name="update"),
path('delete/Post/<id>/',views.deleteView,name="delete"),
]
