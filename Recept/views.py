from tri.form.views import edit_object
from tri.table import render_table_to_response, Column

from Recept.models import Receipt


def index(request):
    return render_table_to_response(
        request,
        template='list.html',
        table__model=Receipt,
        table__extra_fields=[
            Column.edit(after=0),
        ],
    )


def edit(request, pk):
    return edit_object(
        request,
        instance=Receipt.objects.get(pk=pk),
    )