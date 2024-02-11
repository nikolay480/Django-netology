from django.shortcuts import render

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
    'smuzi': {
        'яблоко, шт.': 1,
        'сельдерей, шт.': 4,
        'огурец, шт.': 1,
        'вода, мл': 200,
    }
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
def get_recipe(request, dish_name):
    servings = int(request.GET.get("servings", 1))  # Значение по умолчанию для servings
    dish_recipe = DATA.get(dish_name, {})  # Получение рецепта или пустого словаря, если блюдо не найдено
    recipe = {ingredient: amount * servings for ingredient, amount in dish_recipe.items()}  # Новый словарь с учётом servings
    context = {
        'recipe': recipe
    }
    return render(request, 'calculator/index.html', context)

def omlet(request):
    return get_recipe(request, 'omlet')

def pasta(request):
    return get_recipe(request, 'pasta')

def buter(request):
    return get_recipe(request, 'buter')