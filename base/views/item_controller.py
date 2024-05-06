from django.shortcuts import render
from django.views.generic import ListView
from base.models import Item

class IndexListView(ListView):
    model = Item
    template_name = 'pages/index.html'

""" 関数で書いた場合
def index(request):
    object_list = Item.objects.all()
    context = {
        'object_list': object_list,
    }
    return render(request, 'pages/index.html', context)
"""