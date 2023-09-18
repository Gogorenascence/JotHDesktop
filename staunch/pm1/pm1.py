from game_comps.cards import MainDeckCard, PluckDeckCard


i1g1pmf = MainDeckCard( id=1001, name="PantheraMan", series_names=['PantheraMan', 'Nature', 'Brawler'], hp=5, defending=False, enthusiasm=0, effect_text="Deal 2 damage to a foe who has yet to go this round. If you are first to go this round or you have the highest Enthusiasm, draw 1 Pluck and gain 1 HP.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1g1pmf.png", card_type=1001, reactions=[1003], card_tags=[1001] )


i1g1pma = MainDeckCard( id=1002, name="Boisterous Call!", series_names=['PantheraMan', 'Nature', 'Brawler', 'Call'], hp=5, defending=False, enthusiasm=0, effect_text="Gain 1 HP and add 4 to your Focus.", second_effect_text="<Trigger> At the start of the round, add 4 to your Enthusiasm and resolve this Aura in your play.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1g1pma.png", card_type=1002, reactions=[], card_tags=[1001] )


i1g1pmm = MainDeckCard( id=1003, name="Feasting Claw!!", series_names=['PantheraMan', 'Nature', 'Brawler'], hp=5, defending=False, enthusiasm=0, effect_text="Deal 3 piercing damage to a foe. If you are first to go this round or have the highest Enthusiasm, gain 1 HP.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1g1pmm.png", card_type=1003, reactions=[], card_tags=[1001] )


i1g1pme = MainDeckCard( id=1004, name="Black Claw Divide!!!", series_names=['PantheraMan', 'Nature', 'Brawler'], hp=5, defending=False, enthusiasm=17, effect_text="<Target> Foe who has yet to go this round. //<1-5> Deal 2 piercing damage. //<6-11> Deal 3 piercing damage. //<12+> Deal 4 piercing damage. The next player's Move(s) and Ending(s) gain damage minus 1 (damage dealt by those cards is reduced by 1 at the end of their resolutions).", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1g1pme.png", card_type=1004, reactions=[], card_tags=[1002, 1001] )


i1pl01pmi = PluckDeckCard( id=1067, name="Super Panther Claw", series_names=['PantheraMan', 'Nature', 'Brawler'], effect_text="<Limited> If you have no Moves in your play, deal 2 piercing damage to a foe who has yet to go this round. You can not add Moves to your play this round.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl01pmi.png", card_type=1006, card_tags=[1004] )


i1pl01pme = PluckDeckCard( id=1068, name="A Hero’s Entrance", series_names=['PantheraMan', 'Nature', 'Brawler'], effect_text="<Trigger> At the start of the round or during a foe's turn, resolve the main effect of 1 Fighter in your play.", second_effect_text="<C.Trigger> At the start of the round, you go first.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl01pme.png", card_type=1007, card_tags=[1005] )


i1cb1pm = PluckDeckCard( id=1069, name="Rallying Cry", series_names=['PantheraMan', 'Nature', 'Brawler', 'Call'], effect_text="This Comeback counts as a Staunch card in your play (this does not count towards play size).", second_effect_text="<C.Trigger> At the start of the round or during a foe’s turn, add 8 to your Enthusiasm.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1cb1pm.png", card_type=1008, card_tags=[1000] )


pantheraman = [i1g1pmf, i1g1pma, i1g1pmm, i1g1pme, i1pl01pmi, i1pl01pme, i1cb1pm]
