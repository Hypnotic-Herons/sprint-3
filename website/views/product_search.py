from django.shortcuts import render
from django.http import HttpResponse

def search_form(request):
    
    ''' 
	Author: Meghan Debity
	Purpose: Input form for search bar feature
	'''

    return render(request, 'website/search_form.html')

def search(request):

     ''' 
	Author: Meghan Debity
	Purpose: View search request
	'''

    if 'q' in request.GET:
        message = 'You searched for: %r' % request.GET['q']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)