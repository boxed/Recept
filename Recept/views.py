from django.shortcuts import render_to_response
from tri.form.views import edit_object, create_object
from tri.table import render_table_to_response, Column, Link

from Recept.models import Recipe, RecipeForDay


def index(request):
    return render_to_response('index.html')


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
        table__model=RecipeForDay,
    )
