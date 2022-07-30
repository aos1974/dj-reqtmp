from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    'bize': {
        'яйца, шт': 2,
        'сахорная пудра, ст': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def calculator(request, rec):
    template_name = 'calculator/index.html'

    servings = request.GET.get('servings')
    if servings is None:
        servings = 1
    else:
        servings = int(servings)

    if rec in DATA.keys():
        recipe = DATA.get(rec)
        for ingredient, amount in recipe.items():
            recipe[ingredient] = amount * servings

    else:
        recipe = rec

    context =   {
        'recipe': recipe
                }
    return render(request, template_name, context)

def home_view(request):
    template_name = 'calculator/home.html'
    
    pages = {}
    for rec in DATA.keys():
        pages[rec] = '/' + rec +'/'
    
    context = {
        'pages': pages
    }
    return render(request, template_name, context)
