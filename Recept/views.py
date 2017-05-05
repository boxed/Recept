from datetime import date

from collections import defaultdict
from random import shuffle

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from tri.form.views import edit_object, create_object
from tri.table import render_table_to_response, Column, Link

from Recept import weeks_for_year
from Recept.models import Recipe, RecipeForWeek


def index(request):
    year, week, _ = date.today().isocalendar()

    context = dict(
        week=date.today().isocalendar()[1],
        recipes_for_week=get_or_create_plan(year=year, week=week).recipes.all(),
    )

    return render_to_response('index.html', context=context)


def recipe_list(request):
    return render_table_to_response(
        request,
        template='list.html',
        table__model=Recipe,
        table__extra_fields=[
            Column.edit(after=0),
            # TODO there's no delete_object in tri.form!: Column.delete(after=0),
        ],
        links=[
            Link('Create recipe', 'create/')
        ],
    )


def edit_recipe(request, pk):
    return edit_object(
        request,
        instance=Recipe.objects.get(pk=pk),
    )


def create_recipe(request):
    return create_object(
        request,
        model=Recipe,
    )


def history(request):
    return render_table_to_response(
        request,
        template='list.html',
        table__model=RecipeForWeek,
        table__extra_fields=[
            Column.edit(after=0),
        ],
        links=[
            Link('Create plan', 'plan/'),
        ]
    )


def edit_plan(request, pk):
    return edit_object(
        request,
        instance=RecipeForWeek.objects.get(pk=pk),
    )


def get_or_create_plan(year, week):
    try:
        return RecipeForWeek.objects.get(year=year, week=week)
    except RecipeForWeek.DoesNotExist:
        pass

    recipe_to_week = defaultdict(lambda: (0, 0))

    for recipe in Recipe.objects.all():
        recipe_to_week[recipe] = (0, 0)

    for x in RecipeForWeek.objects.all():
        for recipe in x.recipes.all():
            if (x.year, x.week) > recipe_to_week[recipe]:
                recipe_to_week[recipe] = (x.year, x.week)

    recipes_by_week = defaultdict(set)
    for recipe, week in recipe_to_week.items():
        recipes_by_week[week].add(recipe)
    recipes_by_week = [list(x[1]) for x in sorted(recipes_by_week.items())]
    for x in recipes_by_week:
        shuffle(x)

    # now create a new list
    if not RecipeForWeek.objects.exists():
        year = date.today().year
        week = date.today().isocalendar()[1]
    else:
        newest = RecipeForWeek.objects.order_by('-year', '-week')[0]
        year = newest.year
        week = newest.week + 1
        if week > weeks_for_year(year):
            week = 1
            year += 1
    new_week = RecipeForWeek.objects.create(
        year=year,
        week=week,
    )

    # pick from oldest bucket until it's empty, then continue
    for i in range(5):
        while not recipes_by_week[0]:
            del recipes_by_week[0]
        new_week.recipes.add(recipes_by_week[0].pop(0))


def plan(request):
    year, week, _ = date.today().isocalendar()
    get_or_create_plan(year=year, week=week)
    return HttpResponseRedirect('..')
