from .Card import PokemonCard
import random

class Squirtle(PokemonCard):
    def __init__(self):
        super().__init__("물거북","images/WaterTypeCardImages/Squirtle.png",60,1,"풀",True,"어니거북")
        self.skill_a_cost = 1

    def skill_a(self):
        return ("물대포", 20)

    def evolution(self, deck):
        for idx, card in enumerate(deck.cards):
            if card.name == self.next_evolution:
                evolved = deck.cards.pop(idx)
                evolved.currentHp = evolved.maxHp - (self.maxHp - self.currentHp)
                evolved.currentEnergy = self.currentEnergy
                evolved.turn_summoned = self.turn_summoned
                if deck.battlePokemon == self:
                    deck.battlePokemon = evolved
                else:
                    for i in range(len(deck.BenchPokemons)):
                        if deck.BenchPokemons[i] == self:
                            deck.BenchPokemons[i] = evolved
                            break
                return

class Wartortle(PokemonCard):
    def __init__(self):
        super().__init__("어니거북","images/WaterTypeCardImages/Wartortle.png",80,1,"풀", False,"거북킹")
        self.skill_a_cost = 2

    def skill_a(self):
        return ("스플래시", 40)

    def evolution(self, deck):
        for idx, card in enumerate(deck.cards):
            if card.name == self.next_evolution:
                evolved = deck.cards.pop(idx)
                evolved.currentHp = evolved.maxHp - (self.maxHp - self.currentHp)
                evolved.currentEnergy = self.currentEnergy
                evolved.turn_summoned = self.turn_summoned
                if deck.battlePokemon == self:
                    deck.battlePokemon = evolved
                else:
                    for i in range(len(deck.BenchPokemons)):
                        if deck.BenchPokemons[i] == self:
                            deck.BenchPokemons[i] = evolved
                            break
                return

class Blastoise(PokemonCard):
    def __init__(self):
        super().__init__("거북킹","images/WaterTypeCardImages/Blastoise.png",180,3,"풀", False,"None")
        self.skill_a_cost = 2
        self.skill_b_cost = 3

    def skill_a(self):
        return ("파도타기", 40)

    def skill_b(self):
        return ("하이드로바주카", 120)

class Psyduck(PokemonCard):
    def __init__(self):
        super().__init__("물오리","images/WaterTypeCardImages/Psyduck.png", 60,1,"풀",True,"오리킹")
        self.skill_a_cost = 1

    def skill_a(self):
        return ("두통", 10)

    def evolution(self, deck):
        for idx, card in enumerate(deck.cards):
            if card.name == self.next_evolution:
                evolved = deck.cards.pop(idx)
                evolved.currentHp = evolved.maxHp - (self.maxHp - self.currentHp)
                evolved.currentEnergy = self.currentEnergy
                evolved.turn_summoned = self.turn_summoned
                if deck.battlePokemon == self:
                    deck.battlePokemon = evolved
                else:
                    for i in range(len(deck.BenchPokemons)):
                        if deck.BenchPokemons[i] == self:
                            deck.BenchPokemons[i] = evolved
                            break
                return

class Golduck(PokemonCard):
    def __init__(self):
        super().__init__("오리킹","images/WaterTypeCardImages/Golduck.png",90,1,"풀",False,"None")
        self.skill_a_cost = 2

    def skill_a(self):
        return ("아쿠아에지", 70)

class Pyukumuku(PokemonCard):
    def __init__(self):
        super().__init__("해삼","images/WaterTypeCardImages/Pyukumuku.png",70,1,"풀",True,"None")
        self.skill_a_cost = 1

    def skill_a(self):
        return ("물뿌리기", 30)

class Lapras(PokemonCard):
    def __init__(self):
        super().__init__("라프랄스","images/WaterTypeCardImages/Lapras.png",100,2,"풀",True,"None")
        self.skill_a_cost = 1

    def skill_a(self):
        if self.currentEnergy >= 4:
            return ("하이드로펌프", 90)  # 20 + 70 추가
        return ("하이드로펌프", 20)

class Articuno(PokemonCard):
    def __init__(self):
        super().__init__("빙새","images/WaterTypeCardImages/Articuno.png",100,1,"풀",True,"None")
        self.skill_a_cost = 3

    def skill_a(self):
        return ("냉동빔", 100)
