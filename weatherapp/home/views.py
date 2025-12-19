from django.shortcuts import render


# Create your views here.

# simple function based view which will only render the front end
def home(request):
    return render(request, 'home/home.html')