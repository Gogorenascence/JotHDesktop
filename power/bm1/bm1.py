from game_comps.cards import MainDeckCard, PluckDeckCard


i1r1bmf = MainDeckCard( id=1017, name="Blast Mouth", series_names=['Blast Mouth', 'Altered', 'Nature'], hp=5, defending=False, enthusiasm=0, effect_text="Deal 2 damage to a foe. If you are last to go this round or have the lowest Enthusiasm, deal 1 additional damage and draw 1 Pluck.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1r1bmf.png", card_type=1001, reactions=[1002, 1002], card_tags=[1001] )


i1r1bma = MainDeckCard( id=1018, name="Berserk Transformation!", series_names=['Blast Mouth', 'Altered', 'Nature', 'Transformation'], hp=5, defending=False, enthusiasm=0, effect_text="The next card in your play gains damage plus 1 (that card deals 1 additional damage at the end of its resolution). ", second_effect_text="<Trigger> If you take damage, resolve 1 other random card in your play. If the resolved card targets a foe(s), the target is now 1 random foe.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1r1bma.png", card_type=1002, reactions=[], card_tags=[1001] )


i1r1bmm = MainDeckCard( id=1019, name="Cinder Crunch!!", series_names=['Blast Mouth', 'Altered', 'Nature'], hp=5, defending=False, enthusiasm=0, effect_text="Deal 3 piercing damage to a foe who has already gone this round. If this card defeats a Fighter, your Ending gains damage plus 1 (that card deals 1 additional damage at the end of its resolution).", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1r1bmm.png", card_type=1003, reactions=[], card_tags=[1001] )


i1r1bme = MainDeckCard( id=1020, name="Burning Impact!!!", series_names=['Blast Mouth', 'Altered', 'Nature'], hp=5, defending=False, enthusiasm=6, effect_text="<Target> Foe of your choice. //If you are last to go this round, ignore the reaction(s) of defending Fighter(s). //<1-5> Deal 4 damage. //<6-11> Deal 4 piercing damage. //<12+> Deal 5 piercing damage and 1 additional piercing damage if they have already gone this round.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1r1bme.png", card_type=1004, reactions=[], card_tags=[1002, 1001] )


i1pl05bmi = PluckDeckCard( id=1079, name="Reptilian Super Serum", series_names=['Blast Mouth', 'Altered', 'Nature'], effect_text="Once per round, you can take 2 damage, then your Fighter gains damage plus 1 and is treated as Power for the rest of your turn (that card deals 1 additional damage at the end of its resolution).", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl05bmi.png", card_type=1006, card_tags=[1004] )


i1pl05bme = PluckDeckCard( id=1080, name="Reverting to Normal", series_names=['Blast Mouth', 'Altered', 'Nature', 'Transformation'], effect_text="Add 1 Fighter from the discard pile to your hand.", second_effect_text="<Trigger> If your Fighter would be defeated, return it to your hand instead and add a Fighter with a different class from your hand to your play (this does not count as a defeat; you can not defend with another card this round). ", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl05bme.png", card_type=1007, card_tags=[1005] )


i1cb5bm = PluckDeckCard( id=1081, name="Revenge Swipe", series_names=['Blast Mouth', 'Altered', 'Nature'], effect_text="Take 2 damage, then deal 2 damage to a foe.", second_effect_text="<Critical> Deal 2 piercing damage to a foe.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1cb5bm.png", card_type=1008, card_tags=[1000] )
