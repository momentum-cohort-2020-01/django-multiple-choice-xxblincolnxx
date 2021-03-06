from rest_framework import serializers
from .models import Card, Deck




class CardSerializer(serializers.ModelSerializer):
    # decks = DeckSerializer(many=True)
    class Meta:
        model = Card
        fields = '__all__'

class DeckSerializer(serializers.ModelSerializer):
    cards = CardSerializer(read_only=True, many=True)
    class Meta:
        model = Deck
        fields = '__all__'

