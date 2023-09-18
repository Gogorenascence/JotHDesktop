from game_comps.cards import MainDeckCard, PluckDeckCard


i1p1bnf = MainDeckCard( id=1049, name="Black Note", series_names=['Black Note', 'Altered', 'Quest', 'Call'], hp=5, defending=False, enthusiasm=0, effect_text="All players and their Fighters take 1 damage. Add 3 to your Focus.", second_effect_text="<Trigger> At the start of the round or when this card is revealed, damage you and this card take is reduced by 1. ", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1p1bnf.png", card_type=1001, reactions=[1002, 1002], card_tags=[1001] )


i1p1bna = MainDeckCard( id=1050, name="Debilitating Sound!", series_names=['Black Note', 'Altered', 'Quest', 'Call'], hp=5, defending=False, enthusiasm=0, effect_text="All players discard 1 Move or MAX VARIABLE replacing a Move from their play. If no card was removed from your play, resolve 1 of the discarded Moves from the owner's discard pile.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1p1bna.png", card_type=1002, reactions=[], card_tags=[1001] )


i1p1bnm = MainDeckCard( id=1051, name="Super Sonic Riff!!", series_names=['Black Note', 'Altered', 'Quest', 'Call'], hp=5, defending=False, enthusiasm=0, effect_text="Deal 3 damage to a random foe and you take 2 damage.", second_effect_text="<Trigger> At the start of the round, resolve this Move in your play, then discard it. ", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1p1bnm.png", card_type=1003, reactions=[], card_tags=[1001] )


i1p1bne = MainDeckCard( id=1052, name="Max Reverb!!!", series_names=['Black Note', 'Altered', 'Quest', 'Call'], hp=5, defending=False, enthusiasm=5, effect_text="<Target> All foes. //If you are at 8 HP or less, add 3 to your Focus. //<1-5> Deal 2 piercing damage. Take 4 damage. //<6-11> Deal 3 piercing damage. Take 3 damage. //<12+> Deal 4 piercing damage and ignore the reaction(s) of defending Fighter(s). Take 2 damage.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1p1bne.png", card_type=1004, reactions=[], card_tags=[1002, 1001] )


i1pl13bni = PluckDeckCard( id=1103, name="Earplugs", series_names=['Black Note', 'Altered', 'Quest', 'Call'], effect_text="<Limited> Add 3 to your Focus.", second_effect_text="Once per round, if you or your defending Fighter would take damage from a reaction or self inflicted damage, reduce that damage by 2.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl13bni.png", card_type=1006, card_tags=[1004] )


i1pl13bne = PluckDeckCard( id=1104, name="“1..2..3..”", series_names=['Black Note', 'Altered', 'Quest', 'Call'], effect_text="All players discard cards from their plays until they have 3 or less cards, then deal 2 damage to all players that discarded card(s) from their play. ", second_effect_text="<Critical> All foes and their Fighters take 1 damage.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl13bne.png", card_type=1007, card_tags=[1005] )


i1cb13bn = PluckDeckCard( id=1105, name="Tuning", series_names=['Black Note', 'Altered', 'Quest', 'Call'], effect_text="This Comeback counts as a Canny card in your play (this does not count towards play size).", second_effect_text="<Critical> Add 3 to your Focus.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1cb13bn.png", card_type=1008, card_tags=[1000] )


black_note = [i1p1bnf, i1p1bna, i1p1bnm, i1p1bne, i1pl13bni, i1pl13bne, i1cb13bn]
