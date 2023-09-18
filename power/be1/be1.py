from game_comps.cards import MainDeckCard, PluckDeckCard


i1r3bef = MainDeckCard( id=1025, name="Burst Esper", series_names=['Burst Esper', 'Psychic', 'Energy'], hp=5, defending=False, enthusiasm=0, effect_text="Deal 2 damage to 2 random foes and add 2 to your Focus. Those targeted foes draws 2 cards.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1r3bef.png", card_type=1001, reactions=[1004], card_tags=[1001] )


i1r3bea = MainDeckCard( id=1026, name="Trance State!", series_names=['Burst Esper', 'Psychic', 'Energy'], hp=5, defending=False, enthusiasm=0, effect_text="Discard up to 3 cards from your hand, then add 1 to your Focus for each card discarded. If you discarded 3 cards, resolve 1 of those discarded cards from your discard pile.", second_effect_text="<Trigger> If this card is discarded from your hand or play, deal 2 damage to a random foe.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1r3bea.png", card_type=1002, reactions=[], card_tags=[1001] )


i1r3bem = MainDeckCard( id=1027, name="Mass Conversion and Release!!", series_names=['Burst Esper', 'Psychic', 'Energy'], hp=5, defending=False, enthusiasm=0, effect_text="Discard up to 3 cards from your hand, then deal 1 damage to all foes for each card discarded. If you discarded 3 cards, ignore the reaction(s) of defending Fighter(s).", second_effect_text="<Trigger> If this card is discarded from your hand or play, deal 2 damage to a random foe.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1r3bem.png", card_type=1003, reactions=[], card_tags=[1001] )


i1r3bee = MainDeckCard( id=1028, name="Thermodynamic Break!!!", series_names=['Burst Esper', 'Psychic', 'Energy'], hp=5, defending=False, enthusiasm=13, effect_text="<Target> All foes with a larger hand than you (damage is calculated separately for each target). //<1-5> Deal 1 damage. //<6-11> Deal damage equal to the difference. Draw 1 card. //<12+> Deal damage equal to the difference plus 1. Ignore the reaction(s) of defending Fighter(s). Draw 1 card.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1r3bee.png", card_type=1004, reactions=[], card_tags=[1002, 1001] )


i1pl07bei = PluckDeckCard( id=1085, name="Power Channeling Unit ", series_names=['Burst Esper', 'Psychic', 'Energy'], effect_text="<Limited> Return 1 card from the discard pile to your hand.", second_effect_text="Once per round, if a card in your play or ownership randomly chooses a foe(s) or card(s) at, you choose the target(s) instead. ", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl07bei.png", card_type=1006, card_tags=[1004] )


i1pl07bee = PluckDeckCard( id=1086, name="Testing", series_names=['Burst Esper', 'Psychic', 'Energy'], effect_text="Select 1 card in your play (that card is revealed), then unfurl 5 cards. Add all cards matching that card's class to your hand, then return the other unfurled cards to the top or bottom of the Main deck in any order. ", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl07bee.png", card_type=1007, card_tags=[1005] )


i1cb7be = PluckDeckCard( id=1087, name="Transfer of Bad Energy", series_names=['Burst Esper', 'Psychic', 'Energy', 'Relaxation'], effect_text="Discard 1 card from your hand; 1 random card in your play gains damage plus 1 (that card deals 1 additional damage at the end of its resolution). ", second_effect_text="<C.Trigger> At the start of the round, your Fighter gains Redirect 1 (that card is revealed).", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1cb7be.png", card_type=1008, card_tags=[1000] )
