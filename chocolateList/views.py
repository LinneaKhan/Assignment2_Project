from django.shortcuts import render
from chocolateList.models import ItemChocolateList

def show_chocolateList(request):
    data_chocolateList_item = ItemChocolateList.objects.all()
    context = {
        'list_item': data_chocolateList_item,
        'name': 'Linnea'
    }
    return render(request, "chocolateList.html", context)
