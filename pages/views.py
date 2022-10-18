# from django.shortcuts import render

# # Create your views here.
# # pages/views.py
# from django.views.generic import TemplateView

# class HomePageView(TemplateView):
#     template_name = 'home.html'

# class AboutPageView(TemplateView):
#     template_name = 'about.html'

# pages/views.py
from django.shortcuts import render

def home_page(request):
    return render(request, 'home.html')

def about_page(request):
    return render(request, 'about.html')
