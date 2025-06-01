from .Card import PokemonCard

class Rattata(PokemonCard):
    def __init__(self):
        super().__init__("제리","images/NormalTypeCardImages/Rattata",40,1,"None",True,"빅제리")
        self.skill_a_cost = 1

    def skill_a(self):
        return ("갉기", 20)

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

class Raticate(PokemonCard):
    def __init__(self):
        super().__init__("빅제리","images/NormalTypeCardImages/Raticate",80,1,"None",False,"None")
        self.skill_a_cost = 1

    def skill_a(self):
        return ("물기", 40)
