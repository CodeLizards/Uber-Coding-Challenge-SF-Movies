# Uber-Coding-Challenge-SF-Movies
A simple web app to display where movies have been filmed in SF, filtered by user search
# Uber-Coding-Challenge-SF-Movies
A simple web app to display where movies have been filmed in SF, filtered by user search

<p>I chose to do the SF Movies Project. The goal was to create a web app that shows a map where movies have been filmed in San Francisco where the user should be able to filter the view using an autocompletion search. 
Data Source: https://data.sfgov.org/Culture-and-Recreation/Film-Locations-in-San-Francisco/yitu-d5am;</p>
<li><Hosted: <a href="http://elizabethharris.pythonanywhere.com/index/">SF-Movies-Sites</a>
</li>
<li>Github: https://github.com/CodeLizards/Uber-Coding-Challenge-SF-Movies</li>


<h1>Technical Track</h1>
<p>I started out focused mostly on the backend of this project but I chose the Google Maps Javascript API so I ended up focusing on both front end and backend.</p>

<h1>Tech Used</h1>
<ul>
<li>Languages: Python(some experience)
			   Javascript(little experience)
			   Html(little experience)</li>
<li>Backend Framework: Django(no experience)
    FrontEnd Framework: None</li>
<li>API: Google Maps Javascript API(no experience)</li>
<li>Geocoder: geocode.io</li>
</ul>

<h1>Logic behind Tech Choices:</h1>
Languages: I have some experience with python but I like using python as it is uber's main language I decided it was the best option. There are also a lot of frameworks for web technologies that use python. I have almost no experience with Javascript but I wanted to play around and learn it.

Framework: I chose Django because I have little experience with web frameworks I wanted something that provided a little more structure. It ended up being challenging to understand how the framework works so next time I might choose something with a little more flexibility such as Flask. However, Django provided an easy setup and deployment and I had fun learning it! I used the Sqlite3 Database that comes setup with Django because the daata was relativly simple and I do not have much experience with databases so I wanted something simple and inexpensive to interact with. 

FrontEnd: I only have one html file for the frontend where I embeded javascript for the api. I chose to embed javascript in the html rather than make it its own file because I was using the template language that django provides. With that, I was passing values from the database to the google maps javascript code. 

Geocoder: I decided to batch geocode before putting the data into my database because I didnt want to slow the app down from real time geocoding. Since this was a relatively small scope project and had a preexisting data set, I wanted to keep it simple. 


<h1>How it works</h1>

With the data loaded into a table, the user makes a query to the database which then, if found, gets passed through the views.py into the html where the google maps api draws the map and plots the markers with the found addresses. I was unable to complete the autocompletion in the search bar. I have no experience with jquery and I ran out of time. Also, the boiler plate code provided with django is settings.py, manage.py and the migrations folder. 

<h1>Improvements</h1>
<ul>

<li>I would implement an autocomplete in the search bar using jquery.</li> 

<li>I would do testing. I didn't write any tests for this code because in all honestly I was not not sure what type of testing to do. Testing is so important and fell short in this area. I need to learn more about testing code for web technologies. </li>

<li>I would possibly write it using flask. I did not realize that Django was such a formal framework. I spent two days trying to set up Django and just get the hang of how it is structured.</li>

<li>I also spent a lot of time trying to figure out the google maps geocoding and which api best suited my needs. I played around with the fusion tables api (which I used for the view all button) because I liked the UI and it was not so cluttered with a bunch of markers. However, fusion tables in experimental and does a lot of the work for you which is why I only used it for that button.</li>

<li>I would make the frontend prettier! And maybe implement backbone.js as suggested in challenge.</li>
</ul>
