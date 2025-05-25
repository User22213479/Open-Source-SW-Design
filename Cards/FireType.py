from .Card import PokemonCard

class Charmander(PokemonCard):
    def __init__(self):
        super().__init__("빠이리","images/FireTypeCardImages/Charmander.png",60,1,"물",True,"리자드")
    def skill_a(self):
        pass # 코스트 1 / 불꽃세례 / 20 damage

class Charmeleon(PokemonCard):
    def __init__(self):
        super().__init__("리짜드","images/FireTypeCardImages/Charmeleon.png", 90, 2,"물",False,"리자몽")
    def skill_a(self):
        pass # 코스트 3 / 불꽃의 발톱 / 60 damage / -

class Charizard(PokemonCard):
    def __init__(self):
        super().__init__("리짜몽","images/FireTypeCardImages/Charizard.png", 180, 2, "물", False, "None")
    def skill_a(self):
        pass # 코스트 3 / 베어가르기 / 60 damage
    def skill_b(self):
        pass # 코스트 4 / 홍련의 바람 / 200 damage

class Ponyta(PokemonCard):
    def __init__(self):
        super().__init__("보니타","images/FireTypeCardImages/Ponyta.png", 60,1,"물", True, "날쌩마")
    def skill_a(self):
        pass # 코스트 1 / 불꽃 / 20 damage

class Rapidash(PokemonCard):
    def __init__(self):
        super().__init__("날쌩쌩마","images/FireTypeCardImages/Rapidash.png", 100, 1, "물",False,"None")
    def skill_a(self):
        pass # 코스트 1 / 불꽃의 갈기 / 40 damage

class Salandit(PokemonCard):
    def __init__(self):
        super().__init__("불도마뱀","images/FireTypeCardImages/Salandit.png", 60,1,"물",True,"염뉴트")
    def skill_a(self):
        pass # 코스트 1 / 불꽃엄니 / 10 damage / 동전을 1번 던져서 앞면이 나오면 10 데미지를 추가한다.

class Salazzle(PokemonCard):
    def __init__(self):
        super().__init__("불미호","images/FireTypeCardImages/Salazzle.png",90,1,"물",False,"None")
    def skill_a(self):
        pass # 코스트 2 / 불꽃의 발톱 / 60 damage

class Moltres(PokemonCard):
    def __init__(self):
        super().__init__("불수리","images/FireTypeCardImages/Moltres.png",100,1,"물",True,"None")
    def skill_a(self):
        pass # 코스트 3 / 불새 / 130 damage / 동전을 1번 던져서 앞면이 나오면 이 기술은 실패한다.
