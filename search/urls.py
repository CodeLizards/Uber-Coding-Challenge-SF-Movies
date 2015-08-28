#step 2 of url handling
from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from search.models import Film

urlpatterns = patterns('',
		url(r'^', ListView.as_view(
				queryset=Film.objects.all()[:5], 
				template_name="search.html")),

 )