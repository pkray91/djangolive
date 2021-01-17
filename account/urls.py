from django.urls import path

from account import views

urlpatterns = [

	path('register/',views.register),
	path('adduser/',views.adduser),
	path('login/',views.login),

]