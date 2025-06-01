from Cards.Card import PokemonCard, ItemCard, SupportCard

class Ai:
    def __init__(self):
        self.deck = None
        self.support_used_this_turn = False
        self.turn_counter = 0
        self.manager = None

    def set_manager(self, manager):
        self.manager = manager

    def export_card(self, card):
        console = self.manager.battlescreen.consoleLog

        if isinstance(card, PokemonCard) and not card.is_default:
            for target in [self.deck.battlePokemon] + self.deck.BenchPokemons:
                if target and target.next_evolution == card.name:
                    if getattr(target, "turn_summoned", -1) < self.turn_counter:
                        console.append(f"[AI] {target.name}이(가) {card.name}으로 진화했습니다.")
                        target.evolution(self.deck)
                        return True
                    else:
                        console.append(f"[AI] {target.name}은(는) 이번 턴에 소환되어 진화할 수 없습니다.")
                        return False

        if isinstance(card, PokemonCard) and card.is_default:
            if self.deck.battlePokemon is None:
                self.deck.battlePokemon = card
                card.turn_summoned = self.turn_counter
                console.append(f"[AI] {card.name}을(를) 배틀 몬스터로 배치했습니다.")
                return True
            elif len(self.deck.BenchPokemons) < 3:
                self.deck.BenchPokemons.append(card)
                card.turn_summoned = self.turn_counter
                console.append(f"[AI] {card.name}을(를) 벤치에 배치했습니다.")
                return True
            else:
                console.append("[AI] 벤치가 가득 찼습니다.")
                return False

        if isinstance(card, ItemCard):
            result = None
            try:
                result = card.use(self.deck)
            except TypeError:
                try:
                    result = card.use(self.deck.battlePokemon)
                except TypeError:
                    try:
                        result = card.use()
                    except Exception as e:
                        console.append(f"[AI] 아이템 사용 실패: {str(e)}")
                        return False
            console.append(f"[AI] 아이템 {card.name} 사용: {result}")
            return True

        if isinstance(card, SupportCard):
            if self.support_used_this_turn:
                console.append("[AI] 이번 턴에는 이미 서포트 카드를 사용했습니다.")
                return False
            result = None
            try:
                result = card.use(self.deck)
            except TypeError:
                try:
                    result = card.use(self.deck.battlePokemon)
                except TypeError:
                    try:
                        result = card.use()
                    except Exception as e:
                        console.append(f"[AI] 서포트 카드 사용 실패: {str(e)}")
                        return False
            self.support_used_this_turn = True
            console.append(f"[AI] 서포트 {card.name} 사용: {result}")
            return True

        return False

    def attach_energy(self):
        console = self.manager.battlescreen.consoleLog
        target = self.deck.battlePokemon or (self.deck.BenchPokemons[0] if self.deck.BenchPokemons else None)

        if not target:
            console.append(">> AI: 에너지를 부착할 대상이 없습니다.")
            self.manager.ai_card_export_phase()
            return

        target.currentEnergy += 1
        console.append(f">> AI: {target.name}에게 에너지를 부착했습니다.")
