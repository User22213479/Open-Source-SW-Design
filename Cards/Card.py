class Card: #기본 카드
    def __init__(self, name, img):
        self.name = name
        self.img = "images/FireTypeCardImages/Charmander"
        self.img = img

class PokemonCard(Card):
    def __init__(self,name,img,maxHp,comeback,weakness,is_default, next_evolution):
        super().__init__(name, img)
        self.maxHp = maxHp
        self.currentHp = self.maxHp
        self.currentEnergy = 0
        self.comeback = comeback
        self.weakness = weakness
        self.is_default = is_default
        self.next_evolution = next_evolution
        self.turn_summoned = -1  # 소환된 턴 번호 (진화 제한 조건에 사용)

    def evolution(self, deck, card):
        evolved = card

        # 받은 데미지 계산
        damage_taken = self.maxHp - self.currentHp
        evolved.currentHp = max(evolved.maxHp - damage_taken, 0)

        # 에너지와 턴 정보 유지
        evolved.currentEnergy = self.currentEnergy
        evolved.turn_summoned = self.turn_summoned

        # 위치에 따라 교체 (배틀 or 벤치)
        if deck.battlePokemon is self:
            deck.battlePokemon = evolved
        else:
            for i, p in enumerate(deck.BenchPokemons):
                if p is self:
                    deck.BenchPokemons[i] = evolved
                    break

        return  # 진화 완료 후 종료


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
