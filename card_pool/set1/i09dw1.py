from game_comps.cards import MainDeckCard, PluckDeckCard


i1b1dwa = MainDeckCard( id=1034, name="Double Combatants!", series_names=['Project HERMES', 'Tech', 'Tactical', 'Team'], hp=5, defending=False, enthusiasm=0, effect_text="Draw 1 card. If you have a Fighter in your play, it is now defending. Add 1 Fighter from your hand to your play.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1b1dwa.png", card_type=1002, reactions=[], card_tags=[1001] )


i1b1dwm = MainDeckCard( id=1035, name="Dual Wing Strike!!", series_names=['Project HERMES', 'Tech', 'Tactical', 'Team'], hp=5, defending=False, enthusiasm=0, effect_text="<Target> Your strongest foe. //<1-5> Deal 2 damage. //<6-11> Deal 2 damage. Draw 1 card. //<12+> Deal 2 damage plus 1 additional damage for each card in your play past 4. Add 1 Unity card from the discard pile to your hand.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1b1dwm.png", card_type=1003, reactions=[], card_tags=[1002, 1001] )


i1b1dwf = MainDeckCard( id=1033, name="Jet and Climber", series_names=['Project HERMES', 'Tech', 'Tactical', 'Team'], hp=5, defending=False, enthusiasm=0, effect_text="Add 1 Move or MAX VARIABLE from your hand to your play (MAX VARIABLE counts as a Move). ", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1b1dwf.png", card_type=1001, reactions=[1003], card_tags=[1001] )


i1b1dwe = MainDeckCard( id=1036, name="Dive Bomb Finisher!!!", series_names=['Project HERMES', 'Tech', 'Tactical', 'Team'], hp=5, defending=False, enthusiasm=20, effect_text="<Target> Your weakest foe. //<1-5> Deal 1 damage. //<6-11> Deal 3 damage. //<12+> Deal 1 damage for each card in your play. Return 1 other card in your play to your hand. ", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1b1dwe.png", card_type=1004, reactions=[], card_tags=[1002, 1001] )


i1pl09dwi = PluckDeckCard( id=1091, name="Experimental Dual Mode Thruster", series_names=['Project HERMES', 'Tech', 'Tactical', 'Team'], effect_text="<Trigger> At the start of the round, discard 1 card from your hand; resolve one of the following effects: //<> Add 3 to your Focus for your first Focus roll this round. //<> Add 3 to your Enthusiasm this round.", second_effect_text="Discard this Item after the third round of use.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl09dwi.png", card_type=1006, card_tags=[1004] )


i1pl09dwe = PluckDeckCard( id=1092, name="Project HERMES", series_names=['Project HERMES', 'Tech', 'Tactical', 'Team'], effect_text="Add 1 of the following from their respective discard piles to your hand/ownership: //<>Up to 2 Project cards and 1 Project Pluck except the Event Project HERMES. //<>2 Unity cards. //<>1 MAX VARIABLE and 1 Item.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl09dwe.png", card_type=1007, card_tags=[1005] )


i1cb9dw = PluckDeckCard( id=1093, name="The Survey Crew", series_names=['Project HERMES', 'Tech', 'Tactical', 'Team'], effect_text="This Comeback counts as a Unity card in your play (this does not count towards play size).", second_effect_text="<Critical> Return 1 card from the discard pile to the top of the Main deck.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1cb9dw.png", card_type=1008, card_tags=[1000] )

jet_and_climber = [i1b1dwf, i1b1dwa, i1b1dwm, i1b1dwe, i1pl09dwi, i1pl09dwe, i1cb9dw]
