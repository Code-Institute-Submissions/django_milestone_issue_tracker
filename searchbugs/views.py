from django.shortcuts import render
from bugs.models import Bug

# Create your views here.
def do_search_bugs(request):
    bugs = Bug.objects.filter(name__icontains=request.GET['q'])
    return render(request, "bugs.html", {"bugs": bugs})