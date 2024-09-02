"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('indexPL/', views.index_pl, name='index_pl'),
    path('indexDE/', views.index_de, name='index_de'),

    path('aboutUs/', views.about_us, name='about_us'),
    path('aboutUsDE/', views.about_us_de, name='about_us_de'),
    path('aboutUsPL/', views.about_us_pl, name='about_us_pl'),
    path('comingSoon/', views.coming_soon, name='coming_soon'),
    path('comingSoonDE/', views.coming_soon_de, name='coming_soon_de'),
    path('comingSoonPL/', views.coming_soon_pl, name='coming_soon_pl'),
    path('contact/', views.contact, name='contact'),
    path('contactDE/', views.contact_de, name='contact_de'),
    path('contactPL/', views.contact_pl, name='contact_pl'),
    path('job/', views.job, name='job'),
    path('jobDE/', views.job_de, name='job_de'),
    path('jobPL/', views.job_pl, name='job_pl'),
    path('ourProjects/', views.our_projects, name='our_projects'),
    path('ourProjectsDE/', views.our_projects_de, name='our_projects_de'),
    path('ourProjectsPL/', views.our_projects_pl, name='our_projects_pl'),
    path('Projects/brightSimplicity/',
         views.bright_simplicity, name='bright_simplicity'),
    path('Projects/brightSimplicityDE/',
         views.bright_simplicity_de, name='bright_simplicity_de'),
    path('Projects/brightSimplicityPL/',
         views.bright_simplicity_pl, name='bright_simplicity_pl'),
    path('Projects/futureOnTop/', views.future_on_top, name='future_on_top'),
    path('Projects/futureOnTopDE/',
         views.future_on_top_de, name='future_on_top_de'),
    path('Projects/futureOnTopPL/',
         views.future_on_top_pl, name='future_on_top_pl'),
    path('Projects/greenOasis/', views.green_oasis, name='green_oasis'),
    path('Projects/greenOasisDE/', views.green_oasis_de, name='green_oasis_de'),
    path('Projects/greenOasisPL/', views.green_oasis_pl, name='green_oasis_pl'),
    path('Projects/modernityInGlassWalls/',
         views.modernity_in_glass_walls, name='modernity_in_glass_walls'),
    path('Projects/modernityInGlassWallsDE/',
         views.modernity_in_glass_walls_de, name='modernity_in_glass_walls_de'),
    path('Projects/modernityInGlassWallsPL/',
         views.modernity_in_glass_walls_pl, name='modernity_in_glass_walls_pl'),
    path('Projects/modernTwins/', views.modern_twins, name='modern_twins'),
    path('Projects/modernTwinsDE/', views.modern_twins_de, name='modern_twins_de'),
    path('Projects/modernTwinsPL/', views.modern_twins_pl, name='modern_twins_pl'),
    path('Projects/privateCosiness/',
         views.private_cosiness, name='private_cosiness'),
    path('Projects/privateCosinessDE/',
         views.private_cosiness_de, name='private_cosiness_de'),
    path('Projects/privateCosinessPL/',
         views.private_cosiness_pl, name='private_cosiness_pl'),
    path('Projects/spaceForCreativity/',
         views.space_for_creativity, name='space_for_creativity'),
    path('Projects/spaceForCreativityDE/',
         views.space_for_creativity_de, name='space_for_creativity_de'),
    path('Projects/spaceForCreativityPL/',
         views.space_for_creativity_pl, name='space_for_creativity_pl'),
    path('Projects/strictElegance/', views.strict_elegance, name='strict_elegance'),
    path('Projects/strictEleganceDE/',
         views.strict_elegance_de, name='strict_elegance_de'),
    path('Projects/strictElegancePL/',
         views.strict_elegance_pl, name='strict_elegance_pl'),
    # Добавьте маршруты для остальных страниц по аналогии
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
