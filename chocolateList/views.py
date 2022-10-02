from django.shortcuts import render

def show_chocolateList(request):
    return render(request, "chocolateList.html")
