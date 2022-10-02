from django.urls import path
from chocolateList.views import show_chocolateList

app_name = 'chocolateList'

urlpatterns = [
    path('', show_chocolateList, name='show_chocolateList'),
]