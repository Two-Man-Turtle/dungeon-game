from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.decorators import api_view
from .serializers import ScoreSerializer
from .models import Score
# Create your views here.

class ScoreListView(ListAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer