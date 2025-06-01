from .Card import PokemonCard
import random

class Charmander(PokemonCard):
    def __init__(self):
        super().__init__("빠이리","images/FireTypeCardImages/Charmander.png",60,1,"물",True,"리짜드")
        self.skill_a_cost = 1

    def skill_a(self):
        return ("불꽃세례", 20)

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

class Charmeleon(PokemonCard):
    def __init__(self):
        super().__init__("리짜드","images/FireTypeCardImages/Charmeleon.png", 90, 2,"물",False,"리짜몽")
        self.skill_a_cost = 3

    def skill_a(self):
        return ("불꽃의 발톱", 60)

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

class Charizard(PokemonCard):
    def __init__(self):
        super().__init__("리짜몽","images/FireTypeCardImages/Charizard.png", 180, 2, "물", False, "None")
        self.skill_a_cost = 3
        self.skill_b_cost = 4

    def skill_a(self):
        return ("베어가르기", 60)

    def skill_b(self):
        return ("홍련의 바람", 200)

class Ponyta(PokemonCard):
    def __init__(self):
        super().__init__("보니타","images/FireTypeCardImages/Ponyta.png", 60,1,"물", True, "날쌩쌩마")
        self.skill_a_cost = 1

    def skill_a(self):
        return ("불꽃", 20)

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

class Rapidash(PokemonCard):
    def __init__(self):
        super().__init__("날쌩쌩마","images/FireTypeCardImages/Rapidash.png", 100, 1, "물",False,"None")
        self.skill_a_cost = 1

    def skill_a(self):
        return ("불꽃의 갈기", 40)

class Salandit(PokemonCard):
    def __init__(self):
        super().__init__("불도마뱀","images/FireTypeCardImages/Salandit.png", 60,1,"물",True,"불미호")
        self.skill_a_cost = 1

    def skill_a(self):
        base = 10
        if random.choice([True, False]):
            return ("불꽃엄니", base + 10)
        return ("불꽃엄니", base)

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

class Salazzle(PokemonCard):
    def __init__(self):
        super().__init__("불미호","images/FireTypeCardImages/Salazzle.png",90,1,"물",False,"None")
        self.skill_a_cost = 2

    def skill_a(self):
        return ("불꽃의 발톱", 60)

class Moltres(PokemonCard):
    def __init__(self):
        super().__init__("불수리","images/FireTypeCardImages/Moltres.png",100,1,"물",True,"None")
        self.skill_a_cost = 3

    def skill_a(self):
        if random.choice([True, False]):
            return ("불새", 0)
        return ("불새", 130)
