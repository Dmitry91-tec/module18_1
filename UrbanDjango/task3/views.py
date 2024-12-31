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
    return render(request,'third_task/main_page.html', context)

class class_template(TemplateView):
    template_name = 'third_task/first_page.html'

class class_template_cart(TemplateView):
    template_name = 'third_task/second_page.html'