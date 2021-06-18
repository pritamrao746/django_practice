from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Club


# Create your views here.
def clubs_home_page(request):
    return render(request,'clubs/home.html')

def club_chart_view(request):
    context = {}
    context["query_set"] = Club.objects.all()
    return render(request,'clubs/chart.html',context=context)
