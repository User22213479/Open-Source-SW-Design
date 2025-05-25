from .Card import SupportCard

class DoctorStudy(SupportCard):
    def __init__(self):
        super().__init__("서박사의 연구","images/ItemAndSupportCardImages/DoctorStudy.png")
    def use(self):
        pass # 카드 2장을 뽑는다.

class MinHwa(SupportCard):
    def __init__(self):
        super().__init__("영양제","images/ItemAndSupportCardImages/Minhwa.png")
    def use(self):
        pass # 자신의 배틀 몬스터와 모든 벤치 몬스터들의 HP를 20 회복시킨다.

class Isul(SupportCard):
    def __init__(self):
        super().__init__("물뿌리개","images/ItemAndSupportCardImages/Isul.png")
    def use(self):
        pass # 전투 중인 몬스터가 물타입이라면 에너지 2개를 붙인다.
