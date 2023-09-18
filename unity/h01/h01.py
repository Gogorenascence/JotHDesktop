from game_comps.cards import MainDeckCard, PluckDeckCard


i1b2ha = MainDeckCard( id=1038, name="Clustering!", series_names=['Hive', 'Tech', 'Nature'], hp=5, defending=False, enthusiasm=0, effect_text="Your next Move targets the foes on your left and right instead for its first resolution.", second_effect_text="<Trigger> At the start of the round, discard this Aura in your play; draw 2 cards.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1b2ha.png", card_type=1002, reactions=[], card_tags=[1001] )


i1b2hm = MainDeckCard( id=1039, name="Collection Swarm!!", series_names=['Hive', 'Tech', 'Nature'], hp=5, defending=False, enthusiasm=0, effect_text="Deal 3 damage to a foe, then steal 1 of their Active Items. Discard the Item at the end of the round or when this card is removed from your play.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1b2hm.png", card_type=1003, reactions=[], card_tags=[1001] )


i1b2he = MainDeckCard( id=1040, name="Stinger Tornado!!!", series_names=['Hive', 'Tech', 'Nature'], hp=5, defending=False, enthusiasm=10, effect_text="<Target> 2 foes on your right. //<1-5> Deal 2 damage. //<6-11> Deal 3 piercing damage. //<12+> Deal 3 piercing damage. Reset 1 of your Pluck (you can resolve the extra effects of 1 Pluck one more time).", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1b2he.png", card_type=1004, reactions=[], card_tags=[1002, 1001] )


i1pl10hi = PluckDeckCard( id=1094, name="Self Replicating Mechanical Bees", series_names=['Hive', 'Tech', 'Nature'], effect_text="<Limited> Deal 1 piercing damage to a random foe.", second_effect_text="<Trigger> If you draw a card(s) or gains Pluck(s), gain 1 HP.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl10hi.png", card_type=1006, card_tags=[1004] )


i1pl10he = PluckDeckCard( id=1095, name="Bug in a Cup", series_names=['Hive', 'Tech', 'Nature'], effect_text="<Trigger> If a foe adds a face-up card(s) to their play, discard 1 Item in your ownership; add that card (max of 1) to your play instead and they draw 2 cards. Discard the added card at the end of the round. ", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1pl10he.png", card_type=1007, card_tags=[1005] )


i1cb10h = PluckDeckCard( id=1096, name="Robbing", series_names=['Hive', 'Tech', 'Nature'], effect_text="Draw 2 cards, then 2 random foes draw 1 card.", second_effect_text="<Critical> Steal 1 Pluck from a foe, then they draw 2 cards. Discard the Pluck at the end of your turn or when this Comeback is removed from your ownership.", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1cb10h.png", card_type=1008, card_tags=[1000] )


i1b2hf = MainDeckCard( id=1037, name="Hive", series_names=['Hive', 'Tech', 'Nature'], hp=5, defending=False, enthusiasm=0, effect_text="Draw 1 Pluck and reveal it; apply the following effects based on the Pluck revealed: //<Item> Add 1 Move or MAX VARIABLE from your hand to your play (MAX VARIABLE counts as an Move). //<Event> Reset 1 of your Pluck. //<Comeback> Add 1 Aura, Move or MAX VARIABLE from the discard pile to your hand.", second_effect_text="", effect="Effect Value", second_effect="Second Effect Value", picture_url="https://playmakercards.s3.us-west-1.amazonaws.com/i1b2hf.png", card_type=1001, reactions=[1002, 1002], card_tags=[1001] )
