from django.shortcuts import render

from azizbek.models import About, Category, Portfolio, Profile


def index(request):
    about = About.objects.all()
    profiles = Profile.objects.filter(about=about)
    categories = Category.objects.all()
    works = Portfolio.objects.all()
    context = {
        'about':about,
        'profiles': profiles,
        'categories':categories,
        'works':works,
    }

    return render(request, 'index.html', context)
