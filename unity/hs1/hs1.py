from game_comps.cards import MainDeckCard, PluckDeckCard


i1b3hsf = MainDeckCard( id=1041, name="Hammerspace", series_names=['Warp Family', 'Cosmic', 'Psychic'], hp=5, defending=False, enthusiasm=0, effect_text="Draw 1 card and gain 1 Item. If you have a Canny card in your play, reset 1 of your Pluck (you can resolve the extra effects of 1 Pluck one more time).", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1b3hsf.png", card_type=1001, reactions=[1002, 1004], card_tags=[1001] )


i1b3hsa = MainDeckCard( id=1042, name="Personal Pocket Dimension!", series_names=['Warp Family', 'Cosmic', 'Psychic'], hp=5, defending=False, enthusiasm=0, effect_text="Resolve 1 of the following effects for each Item in your Active Pluck or for each different class in your play://1+: Draw 1 Pluck.//2+: Add 1 Aura from your hand to your play.//3+: Add 1 Move from the discard pile to your play.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1b3hsa.png", card_type=1002, reactions=[], card_tags=[1001] )


i1b3hsm = MainDeckCard( id=1043, name="...And The Kitchen Sink!!", series_names=['Warp Family', 'Cosmic', 'Psychic'], hp=5, defending=False, enthusiasm=0, effect_text="Deal 2 damage to a foe. If you have 4 or more Items in your ownership, deal 2 additional damage.", second_effect_text="<Trigger> At the start of the round, discard this Move in your play; draw 1 Pluck.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1b3hsm.png", card_type=1003, reactions=[], card_tags=[1001] )


i1b3hse = MainDeckCard( id=1044, name="Super Heavyweight Drop!!!", series_names=['Warp Family', 'Cosmic', 'Psychic'], hp=5, defending=False, enthusiasm=9, effect_text="<Target> Foe of your choice. //If you have a Canny card in your play, add 3 to your focus. //<1-5> Deal 3 damage and they gain 1 Item. Gain 1 Item. //<6-11> Deal 4 damage and they draw 1 Pluck. Gain 1 Item. //<12+> Deal 5 damage. Gain 1 Item or add 1 Item from the discard pile to your ownership.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1b3hse.png", card_type=1004, reactions=[], card_tags=[1002, 1001] )


i1pl11hsi = PluckDeckCard( id=1097, name="Infinite Storage Space", series_names=['Warp Family', 'Cosmic', 'Psychic'], effect_text="<Limited> Draw 1 Pluck.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl11hsi.png", card_type=1006, card_tags=[1004] )


i1pl11hse = PluckDeckCard( id=1098, name="“Port!”", series_names=['Warp Family', 'Cosmic', 'Psychic', 'Call'], effect_text="Unfurl 3 cards; add 1 Warp Family series card and 1 Canny card to your hand. Discard the other unfurled cards.", second_effect_text="Add 1 random Warp Family series card or random 1 Canny card from your hand to your play.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl11hse.png", card_type=1007, card_tags=[1005] )


i1cb11hs = PluckDeckCard( id=1099, name="Entering the Inventory", series_names=['Warp Family', 'Cosmic', 'Psychic'], effect_text="Discard 1 card from your hand, then unfurl 2 Pluck. Add 1 Pluck to your ownership and discard the other unfurled Pluck.", second_effect_text="<Critical> Draw 1 card and gain 1 Item.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1cb11hs.png", card_type=1008, card_tags=[1000] )
