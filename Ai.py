from Cards.Card import PokemonCard, ItemCard, SupportCard
import random

class Ai:
    def __init__(self):
        self.deck = None
        self.support_used_this_turn = False
        self.turn_counter = 0
        self.manager = None

    def set_manager(self, manager):
        self.manager = manager

    def export_card(self, card):
        if isinstance(card, PokemonCard) and not card.is_default:
            for target in [self.deck.battlePokemon] + self.deck.BenchPokemons:
                if target and target.next_evolution == card.name:
                    if getattr(target, "turn_summoned", -1) < self.turn_counter:
                        target.evolution(self.deck)
                        self.manager.battlescreen.update_field_display()
                        return True
                    else:
                        return False

        if isinstance(card, PokemonCard) and card.is_default:
            if self.deck.battlePokemon is None:
                self.deck.battlePokemon = card
                card.turn_summoned = self.turn_counter
                self.manager.battlescreen.update_field_display()
                return True
            elif len(self.deck.BenchPokemons) < 3:
                self.deck.BenchPokemons.append(card)
                card.turn_summoned = self.turn_counter
                self.manager.battlescreen.update_field_display()
                return True
            else:
                return False

        if isinstance(card, ItemCard):
            try:
                card.use(self.deck)
            except:
                pass
            return True

        if isinstance(card, SupportCard):
            if self.support_used_this_turn:
                return False
            try:
                card.use(self.deck)
            except:
                pass
            self.support_used_this_turn = True
            return True

        return False

    def export_card_phase(self):
        cards_played = 0
        for card in self.deck.drawCards[:]:
            if self.export_card(card):
                self.deck.drawCards.remove(card)
                cards_played += 1
                self.manager.battlescreen.update_field_display()  # 진화 시 이미지 갱신
                if cards_played >= 2:
                    break
        self.manager.battlescreen.update_field_display()
        if cards_played == 0:
            self.manager.battlescreen.consoleLog.append(">> AI는 낼 수 있는 카드가 없어 아무 것도 내지 않았습니다.")
        self.manager.battlescreen.consoleLog.append(">> AI의 공격 단계입니다.")

    def attach_energy(self):
        # 배틀 몬스터 우선
        targets = []
        if self.deck.battlePokemon:
            targets.append(self.deck.battlePokemon)
        targets.extend(self.deck.BenchPokemons)

        if targets:
            targets[0].currentEnergy += 1

        self.manager.set_phase("export_card")

    def attack_phase(self, skill_name, damage):
        attacker = self.deck.battlePokemon
        defender = self.manager.player.deck.battlePokemon
        console = self.manager.battlescreen.consoleLog

        if attacker.type == defender.weakness:
            damage += 10
            console.append(">> AI가 약점을 찔렀습니다! 추가 데미지 +10")

        defender.currentHp -= damage
        console.append(f">> AI의 {attacker.name}이(가) {skill_name}으로 {damage} 데미지를 입혔습니다.")

        if defender.currentHp <= 0:
            console.append(f">> 당신의 {defender.name}이(가) 쓰러졌습니다.")
            self.manager.player.deck.battlePokemon = None
            self.manager.ai_score += 1

        self.manager.battlescreen.update_field_display()
        self.manager.end_turn()

