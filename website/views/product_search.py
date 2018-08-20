from django.shortcuts import render

def search_form(request):
    
    ''' 
	Author: Meghan Debity
	Purpose: Input form for search bar feature
	'''
    # Your code
    if request.method == 'GET': # If the form is submitted

        search_query = request.GET.get('search_box', None)
        # Do whatever you need with the word the user looked for

    # Your code