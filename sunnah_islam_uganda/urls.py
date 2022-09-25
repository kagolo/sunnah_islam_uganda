"""sunnah_islam_uganda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
from  django.conf import settings
from  django.conf.urls.static import  static
from daawa import views

admin.site.site_header="Sunnah_islam_media_project"
admin.site.index_title="Sunnah_islam_media_uganda"
admin.site.site_title="Bring back the love of sunnah"

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',views.manage_favorite_sheikhs,name="All_islam"),
    path("quran", views.manage_quran, name= "quran"),
    path("contact", views.manage_contact, name= "contact"),
    path("episodes", views.manage_episodes, name= "episodes"),
    path("specials", views.manage_specials, name= "specials"),
    path("audios", views.manage_audios, name= "audios"),

    path('favorite_detail/<int:favorite_sheikh_id>/',views.manage_favorite_sheikh_details,name='favorite_detail'),
    path('one_sheikh_detail/<int:lecture_id>/',views.manage_one_sheikh_details,name='one_sheikh_detail'),
    path('islam_serie_detail/<int:serie_lecture_id>/',views.manage_islam_serie_detail,name='islam_serie_detail'),

]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)