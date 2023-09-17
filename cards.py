class MainDeck:
        def __init__(self,
                id,
                name,
                cards,
                ):
                self.id = id
                self.name = name
                self.cards = cards

class PluckDeck:
        def __init__(self,
                id,
                name,
                cards,
                ):
                self.id = id
                self.name = name
                self.cards = cards

class MainDeckCard:
        def __init__(self,
                id,
                name,
                series_names,
                hp,
                defending,
                enthusiasm,
                effect_text,
                second_effect_text,
                effect,
                second_effect,
                picture_url,
                card_type,
                reactions,
                card_tags,
                ):
                self.id = id
                self.name = name
                self.series_names = series_names
                self.hp = hp
                self.defending = defending
                self.enthusiasm = enthusiasm
                self.effect_text = effect_text
                self.second_effect_text = second_effect_text
                self.effect = effect
                self.second_effect = second_effect
                self.picture_url = picture_url
                self.card_type = card_type
                self.reactions = reactions
                self.card_tags = card_tags

class PluckDeckCard:
        def __init__(self,
                id,
                name,
                series_names,
                effect_text,
                second_effect_text,
                effect,
                second_effect,
                picture_url,
                card_type,
                card_tags,
                ):
                self.id = id
                self.name = name
                self.series_names = series_names
                self.effect_text = effect_text
                self.second_effect_text = second_effect_text
                self.effect = effect
                self.second_effect = second_effect
                self.picture_url = picture_url
                self.card_type = card_type
                self.card_tags = card_tags

class MainDiscard:
        def __init__(self,
                cards,
                ):
                self.cards = cards

class PluckDiscard:
        def __init__(self,
                cards,
                ):
                self.cards = cards
