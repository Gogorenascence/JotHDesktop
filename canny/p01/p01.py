from game_comps.cards import MainDeckCard, PluckDeckCard


i1p2pf = MainDeckCard( id=1053, name="Portal", series_names=['Warp Family', 'Cosmic', 'Psychic'], hp=5, defending=False, enthusiasm=0, effect_text="Look at a random foe's hand, then discard 1 card from their hand. That foe draws 1 card.// If you have a Unity card in your play, resolve this card one more time, but the target foe draws 2 cards instead. ", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1p2pf.png", card_type=1001, reactions=[1002, 1004], card_tags=[1001] )


i1p2pa = MainDeckCard( id=1054, name="Teleporting Mastery!", series_names=['Warp Family', 'Cosmic', 'Psychic'], hp=5, defending=False, enthusiasm=0, effect_text="Discard 1 Aura, Move or Ending in a foe's play, then that foe adds 1 random card matching the removed card's type or MAX VARIABLE from their hand to their play (the new card is revealed). ", second_effect_text="<Trigger> During a foe's turn, resolve this Aura in your play.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1p2pa.png", card_type=1002, reactions=[], card_tags=[1001] )


i1p2pe = MainDeckCard( id=1056, name="Distant Drop-off!!!", series_names=['Warp Family', 'Cosmic', 'Psychic'], hp=5, defending=False, enthusiasm=16, effect_text="<Target> Random foe. //If you have a Unity card in your play, add 3 to your focus. //<1-5> Deal 3 damage. //<6-11> Deal 3 damage. Discard 1 card from their hand. //<12+> Deal 3 damage. They discard 1 card from their play.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1p2pe.png", card_type=1004, reactions=[], card_tags=[1002, 1001] )


i1p2pm = MainDeckCard( id=1055, name="Spatial Reversal!!", series_names=['Warp Family', 'Cosmic', 'Psychic'], hp=5, defending=False, enthusiasm=0, effect_text="This card copies the text of a foe's Move on your left or right until the end of your turn (if their Move is face-down, reveal it).", second_effect_text="<Trigger> If you are targeted for damage, your Fighter gains Redirect 1 (that card is revealed).", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1p2pm.png", card_type=1003, reactions=[], card_tags=[1001] )


i1pl14pi = PluckDeckCard( id=1106, name="An Opening to Their Blindspot", series_names=['Warp Family', 'Cosmic', 'Psychic'], effect_text="<Limited> If you have a Canny Fighter in your play, deal 1 bypassing damage to a foe.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl14pi.png", card_type=1006, card_tags=[1004] )


i1pl14pe = PluckDeckCard( id=1107, name="“Hammer!”", series_names=['Warp Family', 'Cosmic', 'Psychic', 'Call'], effect_text="Unfurl 3 cards; add 1 Warp Family series card and 1 Unity card to your hand. Discard the other unfurled cards.", second_effect_text="Add 1 random Warp Family series card or 1 random Unity card from your hand to your play.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl14pe.png", card_type=1007, card_tags=[1005] )


i1cb14p = PluckDeckCard( id=1108, name="Backdoor Exit", series_names=['Warp Family', 'Cosmic', 'Psychic'], effect_text="<Trigger> If a card(s) in your play would be sent to the discard pile during this round, return that card (max of 1) to your hand instead. ", second_effect_text="<Critical> Discard 1 card from 2 random foes' hands.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1cb14p.png", card_type=1008, card_tags=[1000] )


portal = [i1p2pf, i1p2pa, i1p2pm, i1p2pe, i1pl14pi, i1pl14pe, i1cb14p]
