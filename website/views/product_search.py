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
        # variable products is defined by products filtered through title; title_icontains makes the search insensitive to upper/lower case
        products = Product.objects.filter(title__icontains=query)
    except Product.DoesNotExist:
        # if searched product is not in the database, raise error codes
        query = None
        results = None
        raise Http404
    return render(request, 'product/search_result.html', {"results": products,})