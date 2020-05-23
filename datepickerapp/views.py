from django.shortcuts import render
from .forms import DateRangeForm

# Create your views here.

def  homepage(request):
	form = DateRangeForm()
	context = {"form": form}
	return render(request,"datepickerapp/homepage.html",context)
