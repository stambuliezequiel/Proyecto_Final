from django.views.generic import TemplateView
from django.shortcuts import render

class IndexView(TemplateView):
   template_name = 'index.html'




# from django.shortcuts import render

# def index(request):
#     return render(request, 'index.html')