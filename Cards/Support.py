from .Card import SupportCard

class DoctorStudy(SupportCard):
    def __init__(self):
        super().__init__("서박사의 연구","images/ItemAndSupportCardImages/DoctorStudy.png")

    def use(self, deck):
        draw_count = min(2, len(deck.cards))
        drawn = deck.cards[:draw_count]
        deck.drawCards.extend(drawn)
        deck.cards = deck.cards[draw_count:]
        names = ", ".join([card.name for card in drawn])
        return f"다음 카드를 뽑았습니다: {names}"

class MinHwa(SupportCard):
    def __init__(self):
        super().__init__("영양제","images/ItemAndSupportCardImages/Minhwa.png")

    def use(self, field):
        healed = []
        for card in [field.battlePokemon] + field.BenchPokemons:
            if card:
                amount = min(20, card.maxHp - card.currentHp)
                card.currentHp += amount
                healed.append(f"{card.name}(+{amount})")
        return f"회복된 포켓몬: {', '.join(healed)}"

class Isul(SupportCard):
    def __init__(self):
        super().__init__("물뿌리개","images/ItemAndSupportCardImages/Isul.png")

    def use(self, target):
        if target.weakness == "풀":
            target.currentEnergy += 2
            return f"{target.name}에게 에너지를 2개 부여했습니다."
        return f"{target.name}은(는) 물타입이 아닙니다. 효과 없음."
