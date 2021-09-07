from django.shortcuts import render


def index(request):
    title = 'главная'

    context = {
        'title': title,
    }

    return render(request, 'stepshop/index.html', context)


def contacts(request):
    return render(request, 'stepshop/contact.html')


def about(request):
    return render(request, 'stepshop/about.html')
