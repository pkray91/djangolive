from django.shortcuts import render,redirect

from django.http import HttpResponse
from demo.models import Employee
from demo.forms import EmployeeForm
from news.models import NewsModel
from slider.models import SliderModel 
from news_category.models import NewsCategory

def get_news(request):

	data = NewsModel.objects.all().order_by('-id')
	news_cat = NewsCategory.objects.all()
	return render(request,'news.html',{'data':data,'news_cat':news_cat})


def get_category(request,str):

	data = NewsModel.objects.filter(categoty=str)
	return render(request,'categotynews.html',{'data':data})

def adddata(request):#to store data in database
	if request.method == 'GET':
		form = 	EmployeeForm(request.GET or None)
		if form.is_valid():
			form.save()
			#return HttpResponse('done')
			return redirect('/get-data')
	else:
		form = EmployeeForm()
	return render(request,'form.html',{'form':form})

def get_data(request):#to get data from database and show on website

	data = Employee.objects.all()
	# data = Employee.objects.filter().order_by('salary')
	#data = Employee.objects.all().order_by('-salary')
	# data = Employee.objects.filter().order_by('-salary')[:3]
	#data = Employee.objects.filter().order_by('-salary')[2:5]
	return render(request,'tabledata.html',{'store':data})

def delete(request,id):
	#return HttpResponse(id)
	data = Employee.objects.get(id=id)

	data.delete()
	return redirect('/get-data/')

def getdataforedit(request,id):
	data = Employee.objects.get(id=id)

	return render(request,'update.html',{'data':data})

def updatedata(request,id):#to store data in database
	if request.method == 'GET':
		emp = Employee.objects.get(id=id)
		form = 	EmployeeForm(request.GET,instance=emp)
		if form.is_valid():
			form.save()
			#return HttpResponse('done')
			return redirect('/get-data')
	else:
		form = EmployeeForm()
	return render(request,'form.html',{'form':form})


def home(request):

	data = SliderModel.objects.all()
	news_cat = NewsCategory.objects.all()
	return render(request,'index.html',{'data':data,'news_cat':news_cat})

def about(request):
	news_cat = NewsCategory.objects.all()
	return render(request,'about.html',{'news_cat':news_cat})

# def services(request):
# 	return render(request,'services.html')

def contact(request):
	news_cat = NewsCategory.objects.all()
	return render(request,'contact.html',{'news_cat':news_cat})

def test1(request):
	return HttpResponse('Welcome to Django Wourld !!')

def test2(request):
	return HttpResponse('<h1 style="text-align:center;color:red">My name is Harshit <h1>')
	
def test3(request):

	a = 13
	# b = 5
	# c = a+b
	# return HttpResponse(c)

	if a % 2 == 0:
		return HttpResponse('Even no')
	else:
		return HttpResponse('Odd no')


def form(request):
	return render(request,'form.html')

def getdata(request):

	if request.method == 'GET':
		num1 = request.GET.get('num1')
		num2 = request.GET.get('num2')
		add = request.GET.get('add')
		sub = request.GET.get('sub')
		mul = request.GET.get('multiplication')
		div = request.GET.get('div')
		mod = request.GET.get('mod')
		num1 = int(num1)
		num2 = int(num2)

		if add:
			return HttpResponse(num1+num2)
		elif sub:
			return HttpResponse(num1-num2)
		elif mul:
			return HttpResponse(num1*num2)
		elif div:
			return HttpResponse(num1/num2)
		elif mod:
			return HttpResponse(num1%num2)
		else:
			return HttpResponse('Invalid Number')
		# if num % 2 == 0:
		# 	return HttpResponse('Even no')
		# else:
		# 	return HttpResponse('Odd no')