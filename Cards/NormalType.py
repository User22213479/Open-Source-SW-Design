from .Card import PokemonCard

class Rattata(PokemonCard):
    def __init__(self):
        super().__init__("제리","images/NormalTypeCardImages/Rattata",40,1,"None",True,"빅제리")
        self.skill_a_cost = 1

    def skill_a(self):
        return ("갉기", 20)

class Raticate(PokemonCard):
    def __init__(self):
        super().__init__("빅제리","images/NormalTypeCardImages/Raticate",80,1,"None",False,"None")
        self.skill_a_cost = 1

    def skill_a(self):
        return ("물기", 40)
