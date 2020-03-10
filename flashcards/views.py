from django.shortcuts import render
from rest_framework import viewsets
from .models import Card, FigureCard, TextCard, Deck
from .serializers import CardSerializer, FigureCardSerializer, TextCardSerializer, DeckSerializer
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json


class CardView(viewsets.ModelViewSet):
    queryset = Card.objects.select_subclasses()
    serializer_class = CardSerializer


class FigureCardView(viewsets.ModelViewSet):
    """
    Handles routing for POST, PATCH, GET, DELETE, etc.
    """
    queryset = FigureCard.objects.all()
    serializer_class = FigureCardSerializer


class TextCardView(viewsets.ModelViewSet):
    queryset = TextCard.objects.all()
    serializer_class = TextCardSerializer


class DeckView(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer


# @require_POST #POST OR WHATEVER YOURE USING
# @csrf_exempt #IF YOU DONT WANT A CSRF TOKEN
# def json_response_example(request):
#     """
#     used to handle requests for API hits n such
#     """
#     #decode request body
#     data = json.loads(request.body.decode("utf-8"))
#     #find the client
#     client_pk = data.get('clientId')
#     if client_pk is None:
#         return JsonResponse({"status": "error", "message": "clientID is required"})
    
#     client = request.user.clients.filter(pk=client_pk).first()
    
#     #first, check and make sure theres not an open work interval for this user
#     #if no open interval
#         #create a new work interval for user
#     #else
#         #give warning to the user

#     return JsonResponse({"request_data": data})
