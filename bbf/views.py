from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from bbf.models import *

def home(request):
    return render_to_response('home.html')

def file(request): 
    q = ''
    d = ''
    if 'd' in request.GET:
        d = request.GET['d']
        if d == 'Male':
            query = File.objects.filter(sexfemale=0)
        elif d == 'Female':
            query = File.objects.filter(sexfemale=1)  
        else:
            query = File.objects.all()
    else:
        query = File.objects.all() 
    errors = []    
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter valid date.')
        else:
            query = query.filter(startedbowling__lt=q)
#            return render_to_response('file.html',
#                                      {'entries': result, 'date':q, 'division':d})
    #query = File.objects.all()
    return render_to_response('file.html', {'errors': errors, 'entries':query, 'date':q, 'division':d})

    #return render_to_response('file.html', {'entries':q})

def team(request):    
    errors = []    
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter valid date.')
        else:
            result = Team.objects.filter(established__lt=q)
            return render_to_response('team.html',
                                      {'entries': result, 'query':q})
    
       
    query = Team.objects.all()
    return render_to_response('team.html', {'errors': errors, 'entries':query})

def hall(request):    
    q = Hall.objects.all()
    return render_to_response('hall.html', {'entries':q})

def search_form(request):
    return render_to_response('search_form.html')

def search(request):
    errors = []    
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            result = File.objects.filter(playername__icontains=q)
            return render_to_response('search_result.html',
                                      {'files': result, 'query': q})
    return render_to_response('search_form.html', {'errors': errors})

#def date_search(request):
#    errors = []    
#    if 'q' in request.GET:
#        q = request.GET['q']
#        if not q:
#            errors.append('Enter date.')
#        elif len(q) > 20:
#            errors.append('Please enter a valid date.')
#        else:
#            result = File.objects.filter(playername__icontains=q)
#            return render_to_response('search_result.html',
#                                      {'files': result, 'query': q})
#    return render_to_response('file.html', {'errors': errors})

def player_info(request, id):
    q = File.objects.all().filter(id=id)
    #q = q.filter(id=2)
    
    #return HttpResponse(q)
    return render_to_response('player_info.html',{'query':q})

def team_info(request, id):
    q = Team.objects.all().filter(id=id)
    
    #return HttpResponse(q)
    return render_to_response('team_info.html', {'query':q})