from django.urls import path,include
import django.contrib  
from django.contrib.auth import views as  autview
from . import views
app_name = 'mag'
 
urlpatterns = [
	path('', views.home,name='home'),
	path('signup/', views.signup, name='signup'),
	path('login/', autview.LoginView.as_view(), name='login'),
	path('logout/', views.logout, name='logout'),
#autview.LogoutView.as_view(),  name='logout'),
]
