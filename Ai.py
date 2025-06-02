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
        if isinstance(card, PokemonCard) and not card.is_default:
            for target in [self.deck.battlePokemon] + self.deck.BenchPokemons:
                if target and target.next_evolution == card.name:
                    if getattr(target, "turn_summoned", -1) < self.turn_counter:
                        target.evolution(self.deck,card)
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
            result = card.use(self.deck)
            self.manager.battlescreen.consoleLog.append(f">> 아이템 {card.name}을(를) 사용했습니다.")
            self.manager.battlescreen.consoleLog.append(f">> {result}")
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
        targets = []
        if self.deck.battlePokemon:
            targets.append(self.deck.battlePokemon)
        targets.extend(self.deck.BenchPokemons)

        if targets:
            targets[0].currentEnergy += 1

        self.manager.battlescreen.consoleLog.append(f">>AI가 {targets[0].name}에게 에너지를 붙였습니다.")

    def attack(self):
        monster = self.deck.battlePokemon
        enemy = self.manager.player.deck.battlePokemon
        console = self.manager.battlescreen.consoleLog

        if not monster or not enemy:
            self.manager.end_turn()
            return

        # skill_b 우선
        if hasattr(monster, "skill_b") and monster.currentEnergy >= getattr(monster, "skill_b_cost", 999):
            name, damage = monster.skill_b()
        elif monster.currentEnergy >= getattr(monster, "skill_a_cost"):
            name, damage = monster.skill_a()
        else:
            console.append(">> AI는 사용할 수 있는 기술이 없어 턴을 종료합니다.")
            self.manager.end_turn()
            return

        if self.is_weak_against(monster.weakness, enemy.weakness):
            damage += 10
            console.append(">> AI가 약점을 찔렀습니다! 추가 데미지 +10")

        # 공격 실행
        enemy.currentHp -= damage
        console.append(f">> AI의 {monster.name}이(가) {name}으로 {enemy.name}에게 {damage} 데미지를 입혔습니다.")

        if enemy.currentHp <= 0:
            console.append(f">> {enemy.name}이(가) 쓰러졌습니다!")
            self.manager.player.deck.battlePokemon = None
            self.manager.ai_score += 1

            # 벤치 포켓몬 자동 소환
            if self.manager.player.deck.BenchPokemons:
                new_monster = self.manager.player.deck.BenchPokemons.pop(0)
                self.manager.player.deck.battlePokemon = new_monster
                console.append(f">> {new_monster.name}이(가) 전투에 나섭니다.")

        self.manager.battlescreen.update_field_display()
        self.manager.end_turn()

    def is_weak_against(self, atk_type, def_type):
        return (
            (atk_type == "불" and def_type == "풀") or
            (atk_type == "물" and def_type == "불") or
            (atk_type == "풀" and def_type == "물")
        )
