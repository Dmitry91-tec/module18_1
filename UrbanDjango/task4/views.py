from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
def func_template(request):
    title = 'Главная страница'
    text_1 = 'Главная'
    text_2 = 'Магазин'
    text_3 = 'Корзина'
    context = {
        'title': title,
        'text_1': text_1,
        'text_2': text_2,
        'text_3': text_3
    }
    return render(request,'fourth_task/main_page.html', context)

def func_template_first(request):
    first = 'Atomic Heart'
    second = 'Cyberpunk 2077'
    third = 'PayDay 2'
    games = [first, second]
    context = {
        'first': first,
        'second': second,
        'third': third,
        'games': games,
    }
    return render(request,'fourth_task/first_page.html',context)

def func_template_second(request):
    title = 'Корзина'
    context = {
        'title': title
    }
    return render(request, 'fourth_task/second_page.html', context)