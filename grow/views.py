from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Article
from django.contrib.auth.models import User

# Create your views here..


def index(request):
    articles = Article.objects.all()
    content = {
        'articles': articles
    }
    for a in articles:
        print(a)
    return render(request, 'articles.html', content)

def register(request):
    errors = []
    if request.method == 'POST':
        username = request.POST.username
        if not username:
            errors.append("Введите имя пользователя")
        elif len(username) < 5:
            errors.append("Имя пользователя должно содержать не менее 5 символов")

        email = request.POST.email
        if not email:
            errors.append("Введите адрес эл. почты")

        firstname = request.POST.firstname
        if not firstname:
            errors.append("Введите своё имя")

        lastname = request.POST.lastname
        if not lastname:
            errors.append("Введите своё фамилию")

        password = request.POST.password
        if not password:
            errors.append("Введите пароль")
        elif len(password) < 8:
            errors.append("Пароль должен содержать не менее 8 символов")

        confirmpass = request.POST.confirmpass
        if password and (not confirmpass):
            errors.append("Подтвердите пароль")
        elif password != confirmpass:
            errors.append("Пароли не совпадают")

        sameusers = []
        sameusers.append(User.objects.get(username=username))
        sameusers.append(User.objects.get(email=email))

        if sameusers:
            errors.append("Пользователь с таким именем или адресом эл. почты уже существует")

        if errors:
            return render(request, 'register.html', {'errors': errors})

        User.objects.create_user(username=username, email=email, password=password)


    return render(request, 'register.html')

def article(request, id):
    art = Article.objects.get(id=int(id))
    content = {
        'article' : art
    }
    return render(request, 'single.html', content)