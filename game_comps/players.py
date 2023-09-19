from game_comps.boards import board1, board2, board3, board4


class Player:
    def __init__(self,
                name,
                deck,
                hand,
                ownership,
                main_discard,
                pluck_discard,
                play_area,
                active_pluck,
                hp,
                focus,
                enthusiasm,
                mettle,
                second_wind,
                ):
        self.name = name
        self.deck = deck
        self.hand = hand
        self.ownership = ownership
        self.main_discard = main_discard
        self.pluck_discard = pluck_discard
        self.play_area = play_area
        self.active_pluck = active_pluck
        self.hp = hp
        self.focus = focus
        self.enthusiasm = enthusiasm
        self.mettle = mettle
        self.second_wind = second_wind

player1 = Player(
    name="Player1",
    deck={},
    hand=[],
    ownership=[],
    play_area=board1[0],
    active_pluck=board1[1],
    main_discard=[],
    pluck_discard=[],
    hp=16,
    focus=0,
    enthusiasm=0,
    mettle=0,
    second_wind=False,
)

player2 = Player(
    name="Player2",
    deck={},
    hand=[],
    ownership=[],
    play_area=board2[0],
    active_pluck=board2[1],
    main_discard=[],
    pluck_discard=[],
    hp=16,
    focus=0,
    enthusiasm=0,
    mettle=0,
    second_wind=False,
)

player3 = Player(
    name="Player3",
    deck={},
    hand=[],
    ownership=[],
    play_area=board3[0],
    active_pluck=board3[1],
    main_discard=[],
    pluck_discard=[],
    hp=16,
    focus=0,
    enthusiasm=0,
    mettle=0,
    second_wind=False,
)

player4 = Player(
    name="Player4",
    deck={},
    hand=[],
    ownership=[],
    play_area=board4[0],
    active_pluck=board4[1],
    main_discard=[],
    pluck_discard=[],
    hp=16,
    focus=0,
    enthusiasm=0,
    mettle=0,
    second_wind=False,
)

all_players = [player1, player2, player3, player4]
