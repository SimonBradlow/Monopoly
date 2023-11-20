from card import Card
import csv
import random

class Deck():
    """
    Class representing a deck of cards in Monopoly.
    """
    def __init__(self, deck_type: str, cards: list = [], scale: int = 800):
        self.deck_type = deck_type
        self.cards = []

        # Create whichever deck the user specifies upon initialization
        with open('cards.csv', 'r') as card_file:
            cardreader = csv.DictReader(card_file, delimiter = '|')
            for line in cardreader:
                if line['type'] == self.deck_type:
                    # Gather info for each card from csv file, use it to create that card
                    # and add it to cards array
                    card_type = line['type']
                    name = line['name']
                    desc = line['description']
                    category = line['category']
                    effect = line['effect']
                    new_card = Card(card_type, name, desc, category, effect, scale)
                    self.cards.append(new_card)

    def get_cards(self):
        return self.cards

    def draw_card(self):
        # Initial array size, change as cards are drawn
        num_cards = len(self.cards)

        # Draw a card - when a card is drawn, delete it from the array and return it
        # Make sure to change the size of the array too - return None when deck is empty
        if num_cards == 0:
            return None
        else:
            index = random.randint(0, num_cards - 1)
            card = self.cards[index]
            del self.cards[index]
            num_cards = num_cards - 1
            return card
