from game_comps.cards import MainDeckCard, PluckDeckCard


i1r2rff = MainDeckCard( id=1021, name="Red Fist", series_names=['Red Fist', 'Tech', 'Brawler'], hp=5, defending=False, enthusiasm=0, effect_text="Deal 3 damage to your strongest foe, then discard 3 cards from your hand.", second_effect_text="<Trigger> Just before using this card’s reaction(s), remove 3 Counter tokens from this card; draw 3 cards.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1r2rff.png", card_type=1001, reactions=[1002, 1002, 1002], card_tags=[1001] )


i1r2rfa = MainDeckCard( id=1022, name="Double Ki Charge!", series_names=['Red Fist', 'Tech', 'Brawler'], hp=5, defending=False, enthusiasm=0, effect_text="Add 2 to your Focus and your Fighter gains 1 HP. You can discard 1 Aura from your hand to resolve this effect one more time and your next Move gains damage plus 1. ", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1r2rfa.png", card_type=1002, reactions=[], card_tags=[1001] )


i1r2rfm = MainDeckCard( id=1023, name="Ignition Left!!", series_names=['Red Fist', 'Tech', 'Brawler'], hp=5, defending=False, enthusiasm=0, effect_text="<Target> Foe on your left. //<1-5> Deal 1 damage. //<6-11> Deal 3 piercing damage. //<12+> Deal 3 piercing damage. Ignore the reaction(s) of defending Fighter(s) and draw 1 card.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1r2rfm.png", card_type=1003, reactions=[], card_tags=[1002, 1001] )


i1r2rfe = MainDeckCard( id=1024, name="Big Bang Right!!!", series_names=['Red Fist', 'Tech', 'Brawler'], hp=5, defending=False, enthusiasm=18, effect_text="<Target> Foe on your right. //<1-5> Discard 1 card from your hand. //<6-11> Discard 1 card from your hand. //<12+> If your hand has 6 or more cards, deal 6 piercing damage. Ignore the reaction(s) of defending Fighter(s).", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1r2rfe.png", card_type=1004, reactions=[], card_tags=[1002, 1001] )


i1pl06rfi = PluckDeckCard( id=1082, name="Extra-Dexterous Non-Combat Arms", series_names=['Red Fist', 'Tech', 'Brawler', 'Relaxation'], effect_text="If you have a Power Fighter in your play and you discard a card(s) from your hand, you can draw 1 card.", second_effect_text="Discard this Item after drawing 3 cards by this effect.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl06rfi.png", card_type=1006, card_tags=[1004] )


i1pl06rfe = PluckDeckCard( id=1083, name="Bull in a China Shop", series_names=['Red Fist', 'Tech', 'Brawler'], effect_text="Draw 3 cards, then discard 1 card from your hand.", second_effect_text="<Trigger> At the start of the round or during a player’s turn, deal 1 damage to a random foe each time a card(s) is discarded from your hand or removed from your play this round. ", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl06rfe.png", card_type=1007, card_tags=[1005] )


i1cb6rf = PluckDeckCard( id=1084, name="Peaceful Meditation", series_names=['Red Fist', 'Tech', 'Brawler', 'Relaxation'], effect_text="This Comeback counts as a Power card in your play (this does not count towards play size).", second_effect_text="<Trigger> Draw 3 cards, then discard 1 card from your hand.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1cb6rf.png", card_type=1008, card_tags=[1000] )
