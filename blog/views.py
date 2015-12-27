from django.shortcuts import render,get_object_or_404

# Create your views here.
from .models import Post,Stock,TopStock
from .forms import PostFrom

def post_list(request):
	posts = Post.objects.filter(published_date__isnull=False).order_by('-published_date')
	return render(request,'blog/post_list.html',{'posts':posts})

def stock_list(request):
	stocks = Stock.objects.all()
	return render(request,'blog/stock_list.html',{'stocks':stocks})

def topstock_list(request):
	topstocks = TopStock.objects.all()
	return render(request,'blog/stock_list.html',{'topstocks':topstocks})

def post_detail(request,pk):
	post = get_object_or_404(Post,pk=pk)
	return render(request,'blog/post_detail.html',{'post':post})

def post_new(request):
	form = PostFrom()
	return render(request,'blog/post_edit.html',{'form':form})