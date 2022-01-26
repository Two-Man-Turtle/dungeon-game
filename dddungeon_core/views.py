from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from .serializers import ScoreSerializer
from .models import Score
# Create your views here.

def index(request):
    return render(request, 'dddungeon/index.html')

def showCredits(request):
    return render(request, 'dddungeon/credits.html')

def showControls(request):
    return render(request, 'dddungeon/controls.html')

class ScoreListView(ListAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer