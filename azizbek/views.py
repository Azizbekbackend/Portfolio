from django.shortcuts import render
from django.core.mail import message, send_mail
from azizbek.models import About, Category, Portfolio, Profile


def index(request):
    about = About.objects.all()
    profiles = Profile.objects.filter(about=about)
    categories = Category.objects.all()
    works = Portfolio.objects.all()

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        body = request.POST.get("body")

        data = {
            "name":name,
            "email":email,
            "body":body,
            "subject":subject
        }
        
        message = '''
        New message: {}

        From: {}
        '''.format(data["body"],data["email"])
        send_mail(data['subject'] ,message, '',['tillo5255@gmail.com'])

    context = {
        'about':about,
        'profiles': profiles,
        'categories':categories,
        'works':works,
    }

    return render(request, 'index.html', context)
