from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views
from accounts.views import UserDetailView

app_name="accounts"


urlpatterns=[
path('',views.Registration,name="register"),
path('login/',auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
path('logout/',auth_views.LogoutView.as_view(template_name="accounts/logout.html"),name="logout"),
path('Profile/',views.ProfileView,name="profile"),
path('following/',views.followingView,name="following"),
path('followers/',views.followersView,name='followers'),
path('<username>/',UserDetailView.as_view(),name='userdetail')
]
