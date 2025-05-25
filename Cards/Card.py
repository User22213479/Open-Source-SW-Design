class Card: #기본 카드
    def __init__(self, name, img):
        self.name = name
        self.img = "images/FireTypeCardImages/Charmander"
        self.img = img

class PokemonCard(Card):
    def __init__(self,name,img,hp,comeback,weakness,is_default, next_evolution):
        super().__init__(name, img)
        self.hp = hp
        self.comeback = comeback
        self.weakness = weakness
        self.is_default = is_default
        self.next_evolution = next_evolution

    def skill_a(self):
        pass
    def skill_b(self):
        pass
    def evolution(self, deck):
        pass # if self.next_evolution != "None":

class ItemCard(Card): # 상처약, 몬스터볼, 스피드업
    def __init__(self,name,img):
        super().__init__(name,img)
    def use(self):
        pass

class SupportCard(Card): #박사의 연구, 이슬, 민화
    def __init__(self,name,img):
        super().__init__(name,img)
    def use(self):
        pass

