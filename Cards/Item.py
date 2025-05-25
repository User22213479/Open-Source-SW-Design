from .Card import ItemCard

class PokeBall(ItemCard):
    def __init__(self):
        super().__init__("몬스터볼","images/ItemAndSupportCardImages/Pokeball.png")
    def use(self):
        pass # 자신의 덱에서 기본 포켓몬을 랜덤으로 1장 패로 가져온다.

class Potion(ItemCard):
    def __init__(self):
        super().__init__("치료약","images/ItemAndSupportCardImages/Potion.png")
    def use(self):
        pass # 자신의 포켓몬 1마리의 HP를 20 회복