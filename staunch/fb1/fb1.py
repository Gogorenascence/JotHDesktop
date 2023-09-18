from game_comps.cards import MainDeckCard, PluckDeckCard


i1g4fbf = MainDeckCard( id=1013, name="Flamebell", series_names=['Flamebell', 'Magic', 'Quest'], hp=5, defending=False, enthusiasm=0, effect_text="Gain 2 HP, then all foes with a Power card(s) in their play and their Fighters take 1 damage.", second_effect_text="<Trigger> At the start of the round or when this card is revealed, all Power cards gain damage minus 1 (damage dealt by those cards is reduced by 1 at the end of their resolutions).", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1g4fbf.png", card_type=1001, reactions=[1002, 1003], card_tags=[1001] )


i1g4fba = MainDeckCard( id=1014, name="Warm Mending!", series_names=['Flamebell', 'Magic', 'Quest'], hp=5, defending=False, enthusiasm=0, effect_text="Add 1 card from the discard pile to your hand. If the card added was Staunch or Power, gain 2 HP.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1g4fba.png", card_type=1002, reactions=[], card_tags=[1001] )


i1g4fbm = MainDeckCard( id=1015, name="Healing Backfire!!", series_names=['Flamebell', 'Magic', 'Quest'], hp=5, defending=False, enthusiasm=0, effect_text="Gain 2 HP.", second_effect_text="<Trigger> If you take damage, deal 3 damage to all foes with a Power card(s) in their play. ", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1g4fbm.png", card_type=1003, reactions=[], card_tags=[1001] )


i1g4fbe = MainDeckCard( id=1016, name="Restorative Heat!!!", series_names=['Flamebell', 'Magic', 'Quest'], hp=5, defending=False, enthusiasm=11, effect_text="<Target> Foe of your choice. //All foes with a Power card(s) in their play take 1 damage. //<1-5> Deal 3 damage. //<6-11> Deal 3 damage. Gain 1 HP. //<12+> Deal 4 damage. Gain 2 HP and resolve your Aura one more time.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1g4fbe.png", card_type=1004, reactions=[], card_tags=[1002, 1001] )


i1pl04fbi = PluckDeckCard( id=1076, name="Healing Fire", series_names=['Flamebell', 'Magic', 'Quest'], effect_text="One per round, if you resolve an Aura, gain 1 HP.", second_effect_text="<Trigger> If your Fighter would be defeated or removed from your play, discard this Item; your Fighter gains Endure 1 (that card is revealed).", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl04fbi.png", card_type=1006, card_tags=[1004] )


i1pl04fbe = PluckDeckCard( id=1077, name="Supernova", series_names=['Flamebell', 'Magic', 'Quest'], effect_text="All foes with a Power card(s) in their play take 1 damage. All Fighters are treated as Power and all effects that increase damage are cancelled.", second_effect_text="<Trigger> At the start of the round or if you are targeted for damage, resolve this Event in your ownership.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl04fbe.png", card_type=1007, card_tags=[1005] )


i1cb4fb = PluckDeckCard( id=1078, name="Rekindled", series_names=['Flamebell', 'Magic', 'Quest'], effect_text="If a player(s) has a Power card(s) in their play, gain 2 HP.", second_effect_text="<Critical> Resolve your Aura one more time.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1cb4fb.png", card_type=1008, card_tags=[1000] )


flamebell = [i1g4fbf, i1g4fba, i1g4fbm, i1g4fbe, i1pl04fbi, i1pl04fbe, i1cb4fb]
