from .Card import ItemCard
import random

class PokeBall(ItemCard):
    def __init__(self):
        super().__init__("몬스터볼","images/ItemAndSupportCardImages/Pokeball.png")

    def use(self, deck):
        basics = [card for card in deck.cards if getattr(card, 'is_default', False)]
        if basics:
            chosen = random.choice(basics)
            deck.cards.remove(chosen)
            deck.drawCards.append(chosen)
            return f"기본 몬스터 {chosen.name} 카드를 손패로 가져왔습니다."
        return "기본 몬스터가 없습니다."

class Potion(ItemCard):
    def __init__(self):
        super().__init__("치료약","images/ItemAndSupportCardImages/Potion.png")

    def use(self, target):
        healed = min(20, target.maxHp - target.currentHp)
        target.currentHp += healed
        return f"{target.name}의 HP를 {healed}만큼 회복했습니다."
