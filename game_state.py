from game_comps.players import all_players
from card_pool.set1.set1 import card_pool_set1
from decks import all_decks


player_count = input("How many players are there? ")

deck_list = []
for index, deck in enumerate(all_decks):
    deck_list.append(f"{index + 1}: {deck.name}")
print(deck_list)

def get_deck(deck_number):
    if all_decks[int(deck_number)] is not None:
        player_deck = all_decks[int(deck_number) - 1]
    cards = []
    for card_number in player_deck.cards:
        for card in card_pool_set1:
            if card.id == card_number:
                cards.append(card)
    pluck = []
    for card_number in player_deck.cards:
        for card in card_pool_set1:
            if card.id == card_number:
                pluck.append(card)
    player_deck.cards = cards
    player_deck.pluck = pluck
    return player_deck

def game_start():
    active_players = []
    for i in range(int(player_count)):
        active_player = all_players[i]
        deck_number = input(f"What deck will player {i + 1} use? ")
        active_player.deck = get_deck(deck_number)
        while active_player.deck == {} or None:
            deck_number = input(f"What deck will player {i + 1} use? ")
            active_player.deck = get_deck(deck_number)
        active_players.append(
            active_player
        )
    return active_players

print(game_start())
