from game_comps.cards import MainDeckCard, PluckDeckCard


i1r4bgaf = MainDeckCard( id=1029, name="Battle Girl Alice", series_names=['Battle Girl Alice', 'Magic', 'Brawler'], hp=5, defending=False, enthusiasm=0, effect_text="This card gains Counter 1.", second_effect_text="<Trigger> If you defend with this card, Counter damage this card deals is treated as bypassing damage (once only).", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1r4bgaf.png", card_type=1001, reactions=[1002, 1002], card_tags=[1001] )


i1r4bgam = MainDeckCard( id=1031, name="Side Step Counter!!", series_names=['Battle Girl Alice'], hp=5, defending=False, enthusiasm=0, effect_text="<Target> Foe on your right. //<1-5> Remove 1 reaction token from your Fighter. //<6-11> Deal 2 damage. Your Fighter gains Counter 1. //<12+> Deal 2 bypassing damage. Your Fighter gains Counter 1.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1r4bgam.png", card_type=1003, reactions=[], card_tags=[1002, 1001] )


i1r4bgae = MainDeckCard( id=1032, name="Spinning Swallow Tail Deathblow!!!", series_names=['Battle Girl Alice'], hp=5, defending=False, enthusiasm=19, effect_text="<Target> Foe on your left. //<1-5> Remove 2 reaction tokens from your Fighter. //<6-11> Deal 2 damage. Your Fighter gains Redirect 1. //<12+> Deal 2 bypassing damage. Your Fighter gains Redirect 1.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1r4bgae.png", card_type=1004, reactions=[], card_tags=[1002, 1001] )


i1r4bgaa = MainDeckCard( id=1030, name="Battle Girl Transformation!", series_names=['Battle Girl Alice', 'Magic', 'Brawler'], hp=5, defending=False, enthusiasm=0, effect_text="Resolve 1 of the following effects. If you have yet to deal damage this round, resolve 2 different effects instead: <> Your Fighter gains Counter 1. <> Take 2 damage, then your Fighter gains 2 HP. <> Draw 1 Pluck.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1r4bgaa.png", card_type=1002, reactions=[], card_tags=[1001] )


i1cb8bga = PluckDeckCard( id=1090, name="“More Training!”", series_names=['Battle Girl Alice', 'Magic', 'Brawler', 'Call'], effect_text="<Trigger> At the start of the round or during a foe's turn, your Fighter gains 1 HP (that card is revealed).", second_effect_text="<C.Trigger> At the start of the round or during a foe's turn, your Fighter gains Counter 1 (that card is revealed). ", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1cb8bga.png", card_type=1008, card_tags=[1000] )


i1pl08bgai = PluckDeckCard( id=1088, name="“Battle Greaves!”", series_names=['Battle Girl Alice', 'Magic', 'Brawler', 'Call'], effect_text="<Trigger> At the start of the round or during a foe's turn, your Fighter gains Counter 1 (that card is revealed).", second_effect_text="Once per foe's turn, if you have a defending Power Fighter and you are dealt damage, reduce that damage by 1.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl08bgai.png", card_type=1006, card_tags=[1004] )


i1pl08bgae = PluckDeckCard( id=1089, name="Menacingly Cute Pose", series_names=['Battle Girl Alice', 'Magic', 'Brawler'], effect_text="Foes can not use trigger effects or reactions in response to the effects and reactions of your Fighter(s).", second_effect_text="<Trigger> If your Fighter defends, cancel all non-damaging effect(s) of card(s) targeting you until the end of this turn.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl08bgae.png", card_type=1007, card_tags=[1005] )

battle_girl_alice = [i1r4bgaf, i1r4bgaa, i1r4bgam, i1r4bgae, i1pl08bgai, i1pl08bgae, i1cb8bga]
