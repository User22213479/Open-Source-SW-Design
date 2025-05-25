from .Card import PokemonCard

class Squirtle(PokemonCard):
    def __init__(self):
        super().__init__("물거북","images/WaterTypeCardImages/Squirtle.png",60,1,"풀",True,"어니부기")
    def skill_a(self):
        pass # 코스트 1 / 물대포 / 20 damage
    def evolution(self):
        pass # 어니부기로 진화 / 덱에서 어니부기를 트래쉬

class Wartortle(PokemonCard):
    def __init__(self):
        super().__init__("어니거북","images/WaterTypeCardImages/Wartortle.png",80,1,"풀", False,"거북왕")
    def skill_a(self):
        pass # 코스트 2 / 스플래시 / 40 damage
    def evolution(self):
        pass # 거북왕으로 진화 / 덱에서 거북왕을 트래쉬

class Blastoise(PokemonCard):
    def __init__(self):
        super().__init__("거북킹","images/WaterTypeCardImages/Blastoise.png",180,3,"풀", False,"None")
    def skill_a(self):
        pass # 코스트 2 / 파도타기 / 40 damage
    def skill_b(self):
        pass # 코스트 3 / 하이드로바주카 / 120 damage

class Psyduck(PokemonCard):
    def __init__(self):
        super().__init__("물오리","images/WaterTypeCardImages/Psyduck.png", 60,1,"풀",True,"골덕")
    def skill_a(self):
        pass # 코스트 1 / 두통 / 10 damage
    def evolution(self):
        pass # 골덕으로 진화 / 덱에서 골덕을 트래쉬

class Golduck(PokemonCard):
    def __init__(self):
        super().__init__("오리킹","images/WaterTypeCardImages/Golduck.png",90,1,"풀",False,"None")
    def skill_a(self):
        pass # 코스트 2 / 아쿠아에지 / 70 damage

class Pyukumuku(PokemonCard):
    def __init__(self):
        super().__init__("해삼","images/WaterTypeCardImages/Pyukumuku.png",70,1,"풀",True,"None")
    def skill_a(self):
        pass # 코스트 1 / 물뿌리기 / 30 damage

class Lapras(PokemonCard):
    def __init__(self):
        super().__init__("라프랄스","images/WaterTypeCardImages/Lapras.png",100,2,"풀",True,"None")
    def skill_a(self):
        pass # 코스트 1 /하이드로펌프 / 20damage / 에너지 3개가 추가로 붙어 있다면 70 데미지를 추가한다.

class Articuno(PokemonCard):
    def __init__(self):
        super().__init__("빙새","images/WaterTypeCardImages/Articuno.png",100,1,"풀",True,"None")
    def skill_a(self):
        pass # 코스트 3 / 냉동빔 / 100 / 에너지 2개 감소


