from django.shortcuts import render

def post_list(request):
	return render(request, 'blog/post_list.html', {})

def strona2(request):
	return render(request, 'blog/strona2.html', {})

def last_chance(request):
	return render(request, 'blog/ostatnia_szansa.html', {})

# Create your views here.
