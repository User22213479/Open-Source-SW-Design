from .Card import PokemonCard

class Bulbasaur(PokemonCard):
    def __init__(self):
        super().__init__("이상한씨","images/GrassTypeCardImages/Bulbasaur.png",70,1,"불",True,"이상해풀")
    def skill_a(self):
        pass # 2코스트 / 덩굴채찍 / 40 damage

class Ivysaur(PokemonCard):
    def __init__(self):
        super().__init__("이상한풀","images/GrassTypeCardImages/Ivysaur.png",90,2,"불",False,"이상해꽃")
    def skill_a(self):
        pass # 3코스트 / 잎날가르기 / 60 damage

class Venusaur(PokemonCard):
    def __init__(self):
        super().__init__("이상한꽃","images/GrassTypeCardImages/Venusaur.png",190,3,"불",False,"None")
    def skill_a(self):
        pass #  3코스트 / 잎날가르기 / 60 damage
    def skill_b(self):
        pass # 4코스트 / 자이언트 블룸 / 100 damage / 이 포켓몬의 HP를 30 회복

class Exeggcute(PokemonCard):
    def __init__(self):
        super().__init__("알알이","images/GrassTypeCardImages/Exeggcute.png",50,1,"불",True,"나시")
    def skill_a(self):
        pass # 1코스트 / 씨폭탄 / 20 damage

class Exeggutor(PokemonCard):
    def __init__(self):
        super().__init__("알나무","images/GrassTypeCardImages/Exeggutor.png",130,3,"불",False,"None")
    def skill_a(self):
        pass # 1코스트 / 짓밟기 / 30+ / 동전을 1번 던져서 앞면이 나오면 30데미지를 추가한다.

class Skiddo(PokemonCard):
    def __init__(self):
        super().__init__("풀소","images/GrassTypeCardImages/Skiddo.png",70,1,"불",True,"고고트")
    def skill_a(self):
        pass # 1코스트 / 허찌르기 / 40 / 동전을 1번 던져서 뒷면이 나오면 이 기술은 실패한다.

class Gogoat(PokemonCard):
    def __init__(self):
        super().__init__("풀염소","images/GrassTypeCardImages/Gogoat.png",120,2,"불",False,"None")
    def skill_a(self):
        pass # 3코스트 / 잎날가르기 / 70