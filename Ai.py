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

        if hasattr(card, 'comeback') and not card.is_default:
            for target in [self.deck.battlePokemon] + self.deck.BenchPokemons:
                if target and target.name == card.comeback and getattr(target, "turn_summoned", -1) < self.turn_counter:
                    console.append(f"[AI] {target.name}이(가) {card.name}으로 진화했습니다.")
                    target.evolution(self.deck)
                    return True

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

        if isinstance(card, ItemCard):
            card.use()
            console.append(f"[AI] 아이템 {card.name} 사용")
            return True

        if isinstance(card, SupportCard) and not self.support_used_this_turn:
            card.use()
            self.support_used_this_turn = True
            console.append(f"[AI] 서포트 {card.name} 사용")
            return True

        return False
