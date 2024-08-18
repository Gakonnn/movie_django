from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Movie,Genr
# Create your views here.

def index(request,genr='all',page_nm=1):
    if request.user.is_authenticated:
        is_auth = True
        username = request.user.username
    else:
        username = ''
        is_auth = False


    if genr == 'all':
        movie = Movie.objects.all()
    else:
        horror_category = Genr.objects.get(genr=genr)
        movie = Movie.objects.filter(category=horror_category)

    paginator = Paginator(movie,6)
    current_page = paginator.page(page_nm)
    genrs = Genr.objects.all()

    context = {'movies':current_page,
               'genrs':genrs,
               'page_nm':paginator,
               'genr':genr,
               'username':username,
               'is_auth':is_auth}

    return render(request,'main/main.html', context)

def movie_page(request,genr,moox):
    movie = Movie.objects.get(slug=moox)
    context = {'movie':movie}

    return render(request,'main/movie.html',context)

