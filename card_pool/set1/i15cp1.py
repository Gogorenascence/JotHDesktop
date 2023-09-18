from game_comps.cards import MainDeckCard, PluckDeckCard


i1p3cpf = MainDeckCard( id=1057, name="Ceifeira Preta", series_names=['Ceifeira Preta', 'Mystic', 'Quest'], hp=5, defending=False, enthusiasm=0, effect_text="Resolve 1 of the following effects: //<> Gain 1 Comeback and add 1 Fighter from the discard pile to your hand. //<> Discard 2 Comebacks in your ownership; return 3 cards from the discard pile to the top of the Main deck in any order. ", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1p3cpf.png", card_type=1001, reactions=[1004], card_tags=[1001] )


i1p3cpa = MainDeckCard( id=1058, name="Life Cleaving Presence!", series_names=['Ceifeira Preta', 'Mystic', 'Quest'], hp=5, defending=False, enthusiasm=0, effect_text="This card cannot target the same foe twice.// Discard 1 card from your strongest or weakest foe's hand for each Comeback in your ownership (max of 3), then they draw 1 card for each Comeback in their ownership plus 1 (max of 3).", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1p3cpa.png", card_type=1002, reactions=[], card_tags=[1001] )


i1p3cpm = MainDeckCard( id=1059, name="Reaping Dive!!", series_names=['Ceifeira Preta', 'Mystic', 'Quest'], hp=5, defending=False, enthusiasm=0, effect_text="Take 2 damage, then resolve 1 Comeback in your ownership as if you were at critical HP.", second_effect_text="<Trigger> If a card(s) is discarded from your hand or play, gain 1 Comeback and resolve this Move in your play.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1p3cpm.png", card_type=1003, reactions=[], card_tags=[1001] )


i1p3cpe = MainDeckCard( id=1060, name="Psychopomp Chop!!!", series_names=['Ceifeira Preta', 'Mystic', 'Quest'], hp=5, defending=False, enthusiasm=8, effect_text="<Target> Your strongest or weakest foe. //<1-5> Deal 1 damage. //<6-11> Deal 3 damage. Gain 1 Comeback. //<12+> Deal 3 damage. Gain 2 Comebacks, then resolve 1 of your Comebacks as if you were at critical HP.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1p3cpe.png", card_type=1004, reactions=[], card_tags=[1002, 1001] )


i1pl15cpe = PluckDeckCard( id=1110, name="Grimmer Form", series_names=['Ceifeira Preta', 'Mystic', 'Quest', 'Transformation'], effect_text="<Trigger> If you are targeted for damage, apply each of the following effects for each Comeback in your ownership: //<1> Your Fighter is treated as Canny. //<2> Discard 1 card in your strongest or weakest foe's hand. //<3> You can discard 1 card in your play; you are unaffected by the effect(s) of the card targeting you. //<4+> Your next Move and next Ending gain damage plus 1.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl15cpe.png", card_type=1007, card_tags=[1005] )


i1pl15cpi = PluckDeckCard( id=1109, name="Muertorn the Soul Returning Scythe", series_names=['Ceifeira Preta', 'Mystic', 'Quest'], effect_text="Once per round, if you gain a Comeback(s), add 1 Fighter from the discard pile to the top of the Main deck.", second_effect_text="<Trigger> If a card(s) in your play is discarded before resolving its main effect, discard this Item; resolve that card (max of 1) as if it was in your play.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl15cpi.png", card_type=1006, card_tags=[1004] )


i1cb15cp = PluckDeckCard( id=1111, name="Returning Souls", series_names=['Ceifeira Preta', 'Mystic', 'Quest'], effect_text="Add 2 Comebacks from the discard pile to your ownership. You can not resolve them this round. ", second_effect_text="<Critical> Discard 2 cards from your play; add 1 Aura from the discard pile to your play.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1cb15cp.png", card_type=1008, card_tags=[1000] )


ceifeira_preta = [i1p3cpf, i1p3cpa, i1p3cpm, i1p3cpe, i1pl15cpi, i1pl15cpe, i1cb15cp]
