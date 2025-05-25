from .Card import PokemonCard

class Rattata(PokemonCard):
    def __init__(self):
        super().__init__("제리","images/NormalTypeCardImages/Rattata",40,1,"None",True,"레트라")
    def skill_a(self):
        pass # 코스트 1 / 갉기 / 20 damage

class Raticate(PokemonCard):
    def __init__(self):
        super().__init__("빅제리","images/NormalTypeCardImages/Raticate",80,1,"None",False,"None")
    def skill_a(self):
        pass # 코스트 1 / 물기 / 40 damage

