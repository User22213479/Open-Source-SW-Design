from .Card import PokemonCard
import random

class Bulbasaur(PokemonCard):
    def __init__(self):
        super().__init__("이상한씨","images/GrassTypeCardImages/Bulbasaur.png",70,1,"불",True,"이상한풀")
        self.skill_a_cost = 2

    def skill_a(self):
        return ("덩굴채찍", 40)

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

class Ivysaur(PokemonCard):
    def __init__(self):
        super().__init__("이상한풀","images/GrassTypeCardImages/Ivysaur.png",90,2,"불",False,"이상한꽃")
        self.skill_a_cost = 3

    def skill_a(self):
        return ("잎날가르기", 60)

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

class Venusaur(PokemonCard):
    def __init__(self):
        super().__init__("이상한꽃","images/GrassTypeCardImages/Venusaur.png",190,3,"불",False,"None")
        self.skill_a_cost = 3
        self.skill_b_cost = 4

    def skill_a(self):
        return ("잎날가르기", 60)

    def skill_b(self):
        return ("자이언트 블룸", 100, "heal_self_30")

class Exeggcute(PokemonCard):
    def __init__(self):
        super().__init__("알알이","images/GrassTypeCardImages/Exeggcute.png",50,1,"불",True,"알나무")
        self.skill_a_cost = 1

    def skill_a(self):
        return ("씨폭탄", 20)

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

class Exeggutor(PokemonCard):
    def __init__(self):
        super().__init__("알나무","images/GrassTypeCardImages/Exeggutor.png",130,3,"불",False,"None")
        self.skill_a_cost = 1

    def skill_a(self):
        damage = 30
        if random.choice([True, False]):
            damage += 30
        return ("짓밟기", damage)

class Skiddo(PokemonCard):
    def __init__(self):
        super().__init__("풀소","images/GrassTypeCardImages/Skiddo.png",70,1,"불",True,"풀염소")
        self.skill_a_cost = 1

    def skill_a(self):
        if random.choice([True, False]):
            return ("허찌르기", 40)
        return ("허찌르기", 0)

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

class Gogoat(PokemonCard):
    def __init__(self):
        super().__init__("풀염소","images/GrassTypeCardImages/Gogoat.png",120,2,"불",False,"None")
        self.skill_a_cost = 3

    def skill_a(self):
        return ("잎날가르기", 70)
