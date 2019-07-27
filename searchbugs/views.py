from django.shortcuts import render
from django.db.models import Q
from bugs.models import Bug

# Create your views here.
def do_search_bugs(request):
    bugs = Bug.objects.filter(Q(name__icontains=request.GET['q']) | Q(description__icontains=request.GET['q']))
    return render(request, "bugs.html", {"bugs": bugs})
