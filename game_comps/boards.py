class PlayArea:
        def __init__(self,
                fighter_slot,
                aura_slot,
                move_slot,
                ending_slot,
                slot_5,
                slot_6,
                slot_7,
                slot_8,
                ):
                self.fighter_slot = fighter_slot
                self.aura_slot = aura_slot
                self.move_slot = move_slot
                self.ending_slot = ending_slot
                self.slot_5 = slot_5
                self.slot_6 = slot_6
                self.slot_7 = slot_7
                self.slot_8 = slot_8

play_area1 = PlayArea(
        fighter_slot=[],
        aura_slot=[],
        move_slot=[],
        ending_slot=[],
        slot_5={},
        slot_6={},
        slot_7={},
        slot_8={},
)

play_area2 = PlayArea(
        fighter_slot=[],
        aura_slot=[],
        move_slot=[],
        ending_slot=[],
        slot_5={},
        slot_6={},
        slot_7={},
        slot_8={},
)

play_area3 = PlayArea(
        fighter_slot=[],
        aura_slot=[],
        move_slot=[],
        ending_slot=[],
        slot_5={},
        slot_6={},
        slot_7={},
        slot_8={},
)

play_area4 = PlayArea(
        fighter_slot=[],
        aura_slot=[],
        move_slot=[],
        ending_slot=[],
        slot_5={},
        slot_6={},
        slot_7={},
        slot_8={},
)

class ActivePluck:
        def __init__(self,
                slot_1,
                slot_2,
                slot_3,
                slot_4,
                ):
                self.slot_1 = slot_1
                self.slot_2 = slot_2
                self.slot_3 = slot_3
                self.slot_4 = slot_4

active_pluck1 = ActivePluck([],[],[],[])
active_pluck2 = ActivePluck([],[],[],[])
active_pluck3 = ActivePluck([],[],[],[])
active_pluck4 = ActivePluck([],[],[],[])

board1 = [play_area1, active_pluck1]
board2 = [play_area2, active_pluck2]
board3 = [play_area3, active_pluck3]
board4 = [play_area4, active_pluck4]
