from django.shortcuts import render

# Create your views here.

def category_page(request):
    return render(request, 'category.html')
