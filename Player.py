from Cards.Card import PokemonCard, ItemCard, SupportCard
from PyQt5.QtWidgets import QPushButton

class Player:
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
                        console.append(f">> {target.name}이(가) {card.name}으로 진화했습니다!")
                        target.evolution(self.deck, card)
                        self.manager.battlescreen.update_field_display()
                        self.manager.restart_export_timer()
                        return True
                    else:
                        console.append(f">> {target.name}은(는) 이번 턴에 소환되어 진화할 수 없습니다.")
                        return False

        if isinstance(card, PokemonCard) and card.is_default:
            if self.deck.battlePokemon is None:
                self.deck.battlePokemon = card
                card.turn_summoned = self.turn_counter
                console.append(f">> {card.name}을(를) 배틀 몬스터로 내보냈습니다.")
                self.manager.battlescreen.update_field_display()
                self.manager.restart_export_timer()
                return True
            elif len(self.deck.BenchPokemons) < 3:
                self.deck.BenchPokemons.append(card)
                card.turn_summoned = self.turn_counter
                console.append(f">> {card.name}을(를) 벤치에 배치했습니다.")
                self.manager.battlescreen.update_field_display()
                self.manager.restart_export_timer()
                return True
            else:
                console.append(">> 벤치가 가득 찼습니다.")
                return False

        if isinstance(card, ItemCard):
            result = card.use(self.deck)
            console.append(f">> 아이템 {card.name}을(를) 사용했습니다.")
            console.append(f">> {result}")
            self.manager.restart_export_timer()
            return True

        if isinstance(card, SupportCard):
            if self.support_used_this_turn:
                console.append(">> 이번 턴에는 이미 서포트 카드를 사용했습니다.")
                return False
            try:
                result = card.use(self.deck)
            except TypeError:
                try:
                    result = card.use(self.deck.battlePokemon)
                except TypeError:
                    result = card.use()
            self.support_used_this_turn = True
            console.append(f">> 서포트 카드 {card.name}을(를) 사용했습니다.")
            if result:
                console.append(f">> {result}")
            self.manager.restart_export_timer()
            return True

        console.append(">> 해당 카드를 사용할 수 없습니다.")
        return False

    def attach_energy(self):
        console = self.manager.battlescreen.consoleLog
        layout = self.manager.battlescreen.button_area_layout
        console.append(">> 에너지를 부착할 대상을 선택하세요.")
        self.manager.battlescreen.clear_button_area()

        if self.deck.battlePokemon:
            btn = QPushButton(self.deck.battlePokemon.name)
            btn.clicked.connect(lambda _, c=self.deck.battlePokemon: self.attach_energy_to(c))
            layout.addWidget(btn)

        for pokemon in self.deck.BenchPokemons:
            btn = QPushButton(pokemon.name)
            btn.clicked.connect(lambda _, target=pokemon: self.attach_energy_to(target))
            layout.addWidget(btn)

    def attach_energy_to(self, target):
        target.currentEnergy += 1
        self.manager.battlescreen.consoleLog.append(
            f">> {target.name}에게 에너지를 부착했습니다. 현재 에너지: {target.currentEnergy}"
        )
        self.manager.battlescreen.clear_button_area()
        self.manager.set_phase("export_card")

    def attack(self, skill_key):
        monster = self.deck.battlePokemon
        enemy = self.manager.ai.deck.battlePokemon
        console = self.manager.battlescreen.consoleLog
        name, damage = monster.skill_a() if skill_key == "a" else monster.skill_b()

        if self.is_weak_against(monster.weakness, enemy.weakness):
            damage += 10
            console.append(">> 약점을 찔러 추가 데미지 + 10!")

        enemy.currentHp -= damage
        console.append(f">> {monster.name}이(가) {name}을 사용해 {enemy.name}에게 {damage} 데미지를 입혔습니다.")

        if enemy.currentHp <= 0:
            console.append(f">> {enemy.name}이(가) 쓰러졌습니다!")
            self.manager.ai.deck.battlePokemon = None
            self.manager.player_score+=1
            if self.manager.ai.deck.BenchPokemons:
                new_mon = self.manager.ai.deck.BenchPokemons.pop(0)
                self.manager.ai.deck.battlePokemon = new_mon
                console.append(f">> AI의 {new_mon.name}이(가) 전투에 나섭니다!")
            self.manager.battlescreen.update_field_display()
        else:
            self.manager.battlescreen.update_field_display()

        self.manager.end_turn()

    def is_weak_against(self, atk_type, def_type):
        return (
                (atk_type == "불" and def_type == "풀") or
                (atk_type == "물" and def_type == "불") or
                (atk_type == "풀" and def_type == "물")
        )

    def retreat(self, bench_index):
        current = self.deck.battlePokemon
        bench = self.deck.BenchPokemons

        if bench_index < len(bench):
            new_battle = bench.pop(bench_index)
            self.deck.BenchPokemons.append(current)
            self.deck.battlePokemon = new_battle
            current.currentEnergy -= current.comeback

            self.manager.battlescreen.consoleLog.append(f">> {current.name}이(가) 후퇴하고 {new_battle.name}이(가) 전투에 나섰습니다.")
            self.manager.battlescreen.update_field_display()
            self.manager.end_turn()
