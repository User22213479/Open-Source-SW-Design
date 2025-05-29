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

        if hasattr(card, 'comeback') and not card.is_default:
            all_field = [self.deck.battlePokemon] + self.deck.BenchPokemons
            for target in all_field:
                if target and target.name == card.comeback:
                    if getattr(target, "turn_summoned", -1) < self.turn_counter:
                        console.append(f">> {target.name}이(가) {card.name}으로 진화했습니다!")
                        target.evolution(self.deck)
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
                self.manager.restart_export_timer()
                return True
            elif len(self.deck.BenchPokemons) < 3:
                self.deck.BenchPokemons.append(card)
                card.turn_summoned = self.turn_counter
                console.append(f">> {card.name}을(를) 벤치에 배치했습니다.")
                self.manager.restart_export_timer()
                return True
            else:
                console.append(">> 벤치가 가득 찼습니다.")
                return False

        if isinstance(card, ItemCard):
            card.use()
            console.append(f">> 아이템 {card.name}을(를) 사용했습니다.")
            self.manager.restart_export_timer()
            return True

        if isinstance(card, SupportCard):
            if self.support_used_this_turn:
                console.append(">> 이번 턴에는 이미 서포트 카드를 사용했습니다.")
                return False
            card.use()
            self.support_used_this_turn = True
            console.append(f">> 서포트 카드 {card.name}을(를) 사용했습니다.")
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

        console.append(f">> 버튼 개수: {layout.count()}")

    def attach_energy_to(self, target):
        target.currentEnergy += 1
        self.manager.battlescreen.consoleLog.append(f">> {target.name}에게 에너지를 부착했습니다. 현재 에너지: {target.currentEnergy}")
        self.manager.battlescreen.clear_button_area()
        self.manager.set_phase("export_card")  # attach_energy 끝나고 export_card 단계로 진입
