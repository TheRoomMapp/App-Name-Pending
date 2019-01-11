from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#function based view
def home(request):
	html_var = '! f strings Addition to say whatever I want'
	html_ = f"""<!DOCTYPE html>
	<html lang=en>

	<head>
	</head>
	<body>
	<h1>Hello World!, attempt Number 2</h1>
	<p> space for text and stuff {html_var} </p>
	</body>
	</html>

	"""

	#f strings
	return HttpResponse(html_)

#def home(request):
#	return render(request, "home.html", {}) #response