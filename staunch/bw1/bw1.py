from game_comps.cards import MainDeckCard, PluckDeckCard


i1g3bwf = MainDeckCard( id=1009, name="Bone Whisperer", series_names=['Bone Whisperer', 'Mystic', 'Nature'], hp=5, defending=False, enthusiasm=0, effect_text="Resolve 1 of the following effects: //<> Discard up to 3 cards from your hand; gain 1 HP for each card discarded. //<>Discard 3 cards from your hand; unfurl 3 Pluck (reveal 3 cards from the top of the Pluck deck). Add 2 Pluck to your ownership and discard the other unfurled Pluck.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1g3bwf.png", card_type=1001, reactions=[1001], card_tags=[1001] )


i1g3bwa = MainDeckCard( id=1010, name="Spirit Channeling and Union!", series_names=['Bone Whisperer', 'Mystic', 'Nature'], hp=5, defending=False, enthusiasm=0, effect_text="Add 1 Pluck from the discard pile to your Active Pluck. You can not resolve it this round.", second_effect_text="<Trigger> If a card(s) would be discarded from your hand or play, resolve this Aura in your play, then discard this card instead (max of 1).", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1g3bwa.png", card_type=1002, reactions=[], card_tags=[1001] )


i1g3bwm = MainDeckCard( id=1011, name="Umala - Heavy Trampling!!", series_names=['Bone Whisperer', 'Mystic', 'Nature'], hp=5, defending=False, enthusiasm=0, effect_text="You can resolve one additional Event this round.// Deal 1 piercing damage for each Event in your ownership (max of 4) to a random foe, then gain 1 HP.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1g3bwm.png", card_type=1003, reactions=[], card_tags=[1001] )


i1g3bwe = MainDeckCard( id=1012, name="Pitch - Swift Rending!!!", series_names=['Bone Whisperer', 'Mystic', 'Nature'], hp=5, defending=False, enthusiasm=15, effect_text="<Target> Random foe. //<1-5> No effect. //<6-11> Deal 3 damage. Add 1 Event from the discard pile to your ownership. //<12+> Deal 3 piercing damage. Add 1 card and 1 Event from their respective discard piles to your hand/ownership.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1g3bwe.png", card_type=1004, reactions=[], card_tags=[1002, 1001] )


i1pl03bwi = PluckDeckCard( id=1073, name="Spirit Anchor", series_names=['Bone Whisperer', 'Mystic', 'Nature'], effect_text="<Limited> If you resolve an Event this round, place the Event under this Item instead of discarding it at the end of the round (the placed Event(s) count towards your Pluck limit, and if this Item is discarded or changes ownership, the placed Event(s) is discarded).", second_effect_text="The Event(s) under this Item can be resolved one more time; the Event is not discarded at the end of the round.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl03bwi.png", card_type=1006, card_tags=[1004] )


i1pl03bwe = PluckDeckCard( id=1074, name='"Hau, Scout Ahead!"', series_names=['Bone Whisperer', 'Mystic', 'Nature', 'Call'], effect_text="Add 3 to your Focus and reset 1 of your Pluck. Discard up to 2 Pluck in your ownership; select an equal number of foes. Look at their hand(s) and all cards in their play(s), then discard 1 card from their hand(s). ", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl03bwe.png", card_type=1007, card_tags=[1005] )


i1cb3bw = PluckDeckCard( id=1075, name="Reconnection", series_names=['Bone Whisperer', 'Mystic', 'Nature', 'Relaxation'], effect_text="Discard 2 cards from your hand; gain 1 Event.", second_effect_text="<Limited> Draw 1 Pluck and you can resolve one additional Event this round.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1cb3bw.png", card_type=1008, card_tags=[1000] )


bone_whisperer = [i1g3bwf, i1g3bwa, i1g3bwm, i1g3bwe, i1pl03bwi, i1pl03bwe, i1cb3bw]
