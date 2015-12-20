from django.shortcuts import render

# Create your views here.
from .models import Post,Stock

def post_list(request):
	posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
	return render(request,'blog/post_list.html',{'posts':posts})

def stock_list(request):
	stocks = Stock.objects.all()
	return render(request,'blog/stock_list.html',{'stocks':stocks})

