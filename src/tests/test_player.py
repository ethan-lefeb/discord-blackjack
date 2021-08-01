import pytest
from pydealer import Deck
from ..blackjack import Player

def test_calculate_value_with_no_hand_returns_zero():

    # arrange
    subject = Player()
    subject.hand = None

    # act
    actual = subject.calculate_value()

    # assert
    assert actual == 0

def test_calculate_value_with_one_card_hand_returns_between_1_and_11():

    # arrange
    deck = Deck()
    subject = Player()
    subject.hand = deck.deal(1)

    # act
    actual = subject.calculate_value()

    # assert
    assert actual > 0 and actual < 12
