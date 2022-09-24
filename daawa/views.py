from django.http import request
from django.shortcuts import render,redirect
from multiprocessing import context
from.models import(Favorite_sheikhs)

from.favorite_sheikh_selector import(get_favorite_sheikh,get_favorite_sheikhs)
from.all_sheikhs_selector import(get_all_sheikhs,get_lecture)
from.islam_series_selector import(get_islam_serie_lecture,get_islam_series_lectures)
from.islam_serie_episode_selector import(get_islam_episodes_lectures,get_islam_episode_lecture)


# Create your views here.


def manage_favorite_sheikhs(request):
    get_shks = get_favorite_sheikhs()
    get_all_shks = get_all_sheikhs()
    get_all_series_lectures = get_islam_series_lectures()
    

    context={
        "get_shks":get_shks,
        "get_all_shks":get_all_shks,
        "get_all_series_lectures":get_all_series_lectures,
    }
    return render (request,"index.html",context)

def manage_favorite_sheikh_details(request,favorite_sheikh_id):
    get_shk = get_favorite_sheikh(favorite_sheikh_id)

    context={
        "get_shk":get_shk,
    }
    return render (request,"details.html",context)


def manage_one_sheikh_details(request,lecture_id):
    get_one_shk = get_lecture(lecture_id)

    context={
        "get_one_shk":get_one_shk
    }
    return render (request, "one_sheikh_detail.html",context)

def manage_islam_serie_detail(request,serie_lecture_id):
    get_islam_serie = get_islam_serie_lecture(serie_lecture_id)
    get_all_serie_episodes = get_islam_episodes_lectures(get_islam_serie)

    context={
        "get_all_serie_episodes":get_all_serie_episodes,
    }
    return render (request, "islam_series.html",context)

def manage_quran(request):
    return render (request,"artist.html")