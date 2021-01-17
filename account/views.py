from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages

def register(request):

	return render(request,'register.html')

def adduser(request):

	if request.method == 'GET':
		fname = request.GET.get('first_name')
		lname = request.GET.get('last_name')
		uname = request.GET.get('username')
		passwd = request.GET.get('password')
		cpasswd = request.GET.get('cpassword')
		email = request.GET.get('email')
		
		if passwd == cpasswd:
			if User.objects.filter(email=email).exists():
				mes ="Email already exist with us"
				return render(request,'success.html',{'messages':mes})
			elif User.objects.filter(username=uname).exists():
				mes ="User already exist with us"
				return render(request,'success.html',{'messages':mes})
			else:
				user = User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=passwd)
				user.save()
				# mes = messages.info(request,'You have registred successfully')
				mes = "You have registred successfully"
				return render(request,'success.html',{'messages':mes})
		else:
			mes = "Password did not match"
			return render(request,'success.html',{'messages':mes})	
		
def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request, user)
			return redirect('/')
		else:
			mes ="Invalid user name OR password"
			return render(request,'success.html',{'messages':mes})
	else:
		return render(request,'login.html')	


