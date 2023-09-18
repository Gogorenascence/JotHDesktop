from game_comps.cards import MainDeckCard, PluckDeckCard


i1p4gef = MainDeckCard( id=1061, name="Gravity Enforcer", series_names=['Gravity Enforcer', 'Cosmic', 'Tactical'], hp=5, defending=False, enthusiasm=0, effect_text="Foes with Enthusiasm lower than yours can not use reactions. Deal 2 damage to the foe with the lowest Enthusiasm.", second_effect_text="<Trigger> At the start of the round or when this card is revealed, lower the Enthusiasm of all foes by 4.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1p4gef.png", card_type=1001, reactions=[1001], card_tags=[1001] )


i1p4gea = MainDeckCard( id=1062, name="Heavy Aura!", series_names=['Gravity Enforcer', 'Cosmic', 'Tactical'], hp=5, defending=False, enthusiasm=0, effect_text="Foes with Enthusiasm lower than yours take 1 damage after resolving an Aura(s) or drawing a card(s). ", second_effect_text="<Trigger> At the start of the round, lower the Enthusiasm of all foes by 4 and resolve this Aura in your play.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1p4gea.png", card_type=1002, reactions=[], card_tags=[1001] )


i1p4gem = MainDeckCard( id=1063, name="Heavy Radius!!", series_names=['Gravity Enforcer', 'Cosmic', 'Tactical'], hp=5, defending=False, enthusiasm=0, effect_text="Trigger effects can not be used in response to this card. Deal 3 damage to a foe with Enthusiasm lower than yours. They can not use Items or trigger effects during the next player's turn. ", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1p4gem.png", card_type=1003, reactions=[], card_tags=[1001] )


i1p4gee = MainDeckCard( id=1064, name="Infinity Mass Press!!!", series_names=['Gravity Enforcer', 'Cosmic', 'Tactical'], hp=5, defending=False, enthusiasm=14, effect_text="Reduce the Focus of all foes by 4.", second_effect_text="<Target> Foe with Enthusiasm lower than yours. //<1-5> No effect. //<6-11> Deal 4 damage. //<12+> Deal damage equal to the difference (max of 7).", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1p4gee.png", card_type=1004, reactions=[], card_tags=[1002, 1001] )


i1pl16gei = PluckDeckCard( id=1112, name="Gravity Patrol Badge", series_names=['Gravity Enforcer', 'Cosmic', 'Tactical'], effect_text="<L.Trigger> During a foe's turn, card effects can not be resolved more than once this round.", second_effect_text="Lower the Enthusiasm of all foes by 2.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl16gei.png", card_type=1006, card_tags=[1004] )


i1pl16gee = PluckDeckCard( id=1113, name="Ground Collapse", series_names=['Gravity Enforcer', 'Cosmic', 'Tactical'], effect_text="Reduce the focus of all foes by 2. If they have Enthusiasm lower than yours, reduce it by 4 instead.", second_effect_text="<Trigger> At the start of the round, lower the Enthusiasm of all foes by 2, then resolve this Event in your ownership.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl16gee.png", card_type=1007, card_tags=[1005] )


i1cb16ge = PluckDeckCard( id=1114, name="New Equilibrium", series_names=['Gravity Enforcer', 'Cosmic', 'Tactical'], effect_text="<Trigger> At the start of the round or during a foe's turn, lower the Enthusiasm of all foes by 2.", second_effect_text="<Critical> Your Ending gains damage plus 1 if it deals damage to a foe with Enthusiasm lower than yours.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1cb16ge.png", card_type=1008, card_tags=[1000] )


gravity_enforcer = [i1p4gef, i1p4gea, i1p4gem, i1p4gee, i1pl16gei, i1pl16gee, i1cb16ge]
