from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post, Price
from .forms import PriceForm
from django.contrib import messages

poststry= [
	{
		'author': 'CoreyMS',
		'title': 'Blog Post 1',
		'content': 'Firsty post content',
		'date_posted': 'August 27, 2018'
	},
	{
		'author': 'sean',
		'title': 'Blog Post 2',
		'content': 'second post contentttttttttt',
		'date_posted': 'August 28, 2018'
	}

]

girl= [
	{
	'name': 'mayaka',
	'country': 'japan',
	'love': '5'
	}
]

# Create your views here.
def home(request):
	context= {
		'posts': Post.objects.all()
	}
	return render(request, 'info/home.html', context)

def about(request):
	return render(request, 'info/about.html', {'title': 'About'})	

# Create your views here.
def hometry(request):
	context= {
		'posts': poststry,
		'girls': girl
	}
	return render(request, 'info/hometry.html', context)

def abouttry(request):
	return render(request, 'info/abouttry.html', {'title': 'About'})		

def price(request):
	context= {
		'prices': Price.objects.all()
	}
	return render(request, 'info/price.html', context)	

def pricenew(request):
	form= PriceForm(request.POST)
	if form.is_valid():
		form.save()
		name= form.cleaned_data.get('name')
		messages.success(request, f'Hair price created for {name}!')
		return redirect('info-price')


	return render(request, 'info/pricenew.html', {'form': form})	