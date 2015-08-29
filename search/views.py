# Sources:  http://www.djangobook.com/en/2.0/chapter07.html
# 			https://docs.djangoproject.com/en/1.8/
from django.http import HttpResponse
from search.models import Film
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.shortcuts import render_to_response, render
from django.views.generic.base import TemplateView



# Search bar code that makes query to database
def search(request):
    all_films = Film.objects.all()
        all_unique = []
        first = 1
        #Walks through all film entries in db and puts only unique film names in list
        for film in all_films:
            if(first == 1) :
                unique = film
                    first = first+1
                        all_unique.append(film)
                elif(unique.title != film.title):
                    all_unique.append(film)
                        unique = film
    #checks for query from searchbar
    #then puts all results that match the search in list
    if 'post_q' in request.GET and request.GET['post_q']:
        q = request.GET['post_q']
            films = Film.objects.filter(title=q)
            return render(request, 'index.html', { 'films': films, 'all_films': all_films, 'all_unique': all_unique},)
        elif 'q' in request.GET and request.GET['q']:
            q = request.GET['q']
                films = Film.objects.filter(title=q)
                
                return render(request, 'index.html', {'films':films, 'query': q, 'all_films': all_films, 'all_unique': all_unique})
        #if no query made, then just renders the blank map
        else:
            no_result = "You didn't search for anything"
                return render(request, 'index.html', { 'all_films': all_films, 'all_unique': all_unique, 'no_result': no_result})

#This function just renders the form and gives it a list of only
# the unique films so that they can display in drop down menu when first landing on page
# before any query. Same code as above, slightly superfluous.
def index(request):
    all_films = Film.objects.all()
        all_unique = []
        first = 1
        #Walks through all film entries in db and puts only unique film names in list
        for film in all_films:
            if(first == 1):
                unique = film
                    first = first+1
                        all_unique.append(film)
                elif(unique.title != film.title):
                    all_unique.append(film)
                        unique = film
    return render(request, 'index.html', {'all_films':all_films, 'all_unique':all_unique})
