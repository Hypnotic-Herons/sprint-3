from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.template import RequestContext
from . import Product

def search_form(request):
    '''
	Author: Meghan Debity
	Purpose: Input form for search bar feature
	'''
    return render(request, 'product/search_form.html')

def search(request):
    '''
	Author: Meghan Debity
	Purpose: View search request
	'''
    query = request.GET.get('q')
    try:
        products = Product.objects.filter(title__icontains=query)
        print("things", products)
    except Product.DoesNotExist:
        query = None
        results = None
        raise Http404
    return render(request, 'product/search_result.html', {"results": products,})