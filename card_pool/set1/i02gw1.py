from game_comps.cards import MainDeckCard, PluckDeckCard


i1g2gwf = MainDeckCard( id=1005, name="Golden Wall", series_names=['Golden Wall', 'Cosmic', 'Defender'], hp=5, defending=False, enthusiasm=0, effect_text="<Trigger> At the start of the round or when this card is revealed, draw 1 card and this card gains 2 HP.", second_effect_text="<Critical> You can 1 damage to a random foe each time you resolve a Staunch card or defend with this card this round.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1g2gwf.png", card_type=1001, reactions=[1001], card_tags=[1001] )


i1g2gwa = MainDeckCard( id=1006, name="Formation of the Golden Wall!", series_names=['Golden Wall', 'Cosmic', 'Defender', 'Transformation'], hp=5, defending=False, enthusiasm=0, effect_text="Gain 2 HP.", second_effect_text="<Trigger> If you are targeted for damage, your Fighter gains Block 1 (that card is revealed).", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1g2gwa.png", card_type=1002, reactions=[], card_tags=[1001] )


i1g2gwm = MainDeckCard( id=1007, name="Swift Guard!!", series_names=['Golden Wall', 'Cosmic', 'Defender'], hp=5, defending=False, enthusiasm=0, effect_text="<Target> Foe on your left or right. //<1-5> No effect. //<6-11> Deal 2 damage. Damage you and your Fighter take this turn is reduced by 1. //<12+> Deal 3 damage. Damage you and your Fighter take this turn is reduced by 1.", second_effect_text="<Trigger> If you are targeted for damage, resolve this Move in your play.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1g2gwm.png", card_type=1003, reactions=[], card_tags=[1002, 1001] )


i1g2gwe = MainDeckCard( id=1008, name="Double Wall Blowback!!!", series_names=['Golden Wall', 'Cosmic', 'Defender'], hp=5, defending=False, enthusiasm=7, effect_text="<Target> Foes on your left and right. //<1-5> Deal 2 damage. //<6-11> Deal 3 damage and if either target has a defending Fighter, deal 1 bypassing damage to them. //<12+> Deal 3 damage and if either target has a defending Fighter, they both take 1 damage.", second_effect_text="<Trigger> If this card is discarded from your hand or play, your Fighter gains 2 HP (that card is revealed).", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1g2gwe.png", card_type=1004, reactions=[], card_tags=[1002, 1001] )


i1pl02gwi = PluckDeckCard( id=1070, name="Gold Frag", series_names=['Golden Wall', 'Cosmic', 'Defender'], effect_text="<L. Trigger> When a Fighter in your play is revealed, that Fighter gains 1 HP.", second_effect_text="<C. Trigger> If you resolve the trigger effect of a Staunch card in your play, deal 2 damage to a random foe.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl02gwi.png", card_type=1006, card_tags=[1004] )


i1pl02gwe = PluckDeckCard( id=1071, name="“Get Behind Me!”", series_names=['Golden Wall', 'Cosmic', 'Defender', 'Call'], effect_text="<C.Trigger> If you are targeted for damage and your Fighter has 3 or less HP, add 1 card from your hand to your play. The added card takes the damage instead (this does not count as defending). If the card added was a Staunch Fighter, resolve its main effect.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl02gwe.png", card_type=1007, card_tags=[1005] )


i1cb2gw = PluckDeckCard( id=1072, name="New Foundation", series_names=['Golden Wall', 'Cosmic', 'Defender'], effect_text="<Trigger> If you resolve a trigger effect, gain 1 HP.", second_effect_text="<Critical> Gain 2 HP.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1cb2gw.png", card_type=1008, card_tags=[1000] )


golden_wall = [i1g2gwf, i1g2gwa, i1g2gwm, i1g2gwe, i1pl02gwi, i1pl02gwe, i1cb2gw]
