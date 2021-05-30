from django.shortcuts import render

def index(request):
   return render(request,'rasa_view/rasa.html')
