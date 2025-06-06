from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import uic
from Deck import *

battleForm = uic.loadUiType("ui/second.ui")[0]

class BattleScreen(QMainWindow, battleForm):
    def __init__(self, manager):
        super().__init__()
        self.setupUi(self)
        self.manager = manager
        self.button_area_layout = self.buttonArea.layout()
        self.initialize_battle()
        self.Export_Button.clicked.connect(self.on_export_button_clicked)

    def initialize_battle(self):
        self.loadDeck()
        self.setConsole()

    def loadDeck(self):
        self.selected_card = None
        self.cards_per_row = 5
        self.card_width = 150
        self.card_height = 200
        cards = self.manager.player.deck.drawCards

        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.setSpacing(10)

        for card in cards:
            card_button = QPushButton()
            card_button.setCheckable(True)
            try:
                card_image = QPixmap(card.img)
                if card_image.isNull():
                    raise ValueError(f"이미지 로드 실패: {card.img}")
                card_image = card_image.scaled(self.card_width, self.card_height, Qt.KeepAspectRatio)
                card_button.setIcon(QIcon(card_image))
                card_button.setIconSize(card_image.size())
            except Exception:
                card_button.setText(card.name)

            card_button.clicked.connect(lambda checked, btn=card_button, card=card: self.toggleCardSelection(btn, checked, card))
            self.horizontal_layout.addWidget(card_button)

        card_widget = QWidget()
        card_widget.setLayout(self.horizontal_layout)
        card_widget.setMinimumWidth(len(cards) * self.card_width)
        self.scroll_area.setWidget(card_widget)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def toggleCardSelection(self, card_button, checked, card):
        if checked:
            if self.selected_card and self.selected_card != card_button:
                self.selected_card.setStyleSheet("")
                self.selected_card.setChecked(False)
            self.selected_card = card_button
            self.selected_card_data = card
            self.selected_card.setStyleSheet("border: 3px solid green;")
        else:
            if self.selected_card == card_button:
                self.selected_card = None
            card_button.setStyleSheet("")

    def on_export_button_clicked(self):
        if not self.selected_card:
            self.consoleLog.append(">> 카드를 선택해 주세요.")
            return

        card = self.selected_card_data
        success = self.manager.player.export_card(card)

        if success:
            self.consoleLog.append(f">> {card.name} 카드가 성공적으로 내보내졌습니다.")
            self.manager.player.deck.drawCards.remove(card)
            self.refresh_card_area()
            self.update_field_display()
        else:
            self.consoleLog.append(f">> {card.name} 카드를 내보낼 수 없습니다.")

        self.selected_card = None

    def refresh_card_area(self):
        for i in reversed(range(self.horizontal_layout.count())):
            widget = self.horizontal_layout.itemAt(i).widget()
            if widget is not None:
                widget.setParent(None)
        self.loadDeck()

    def clear_button_area(self):
        while self.button_area_layout.count():
            item = self.button_area_layout.takeAt(0)
            if item.widget():
                item.widget().setParent(None)

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().setParent(None)

    def update_field_display(self):
        if self.manager.player.deck.battlePokemon:
            w = self.Player_Battle_Monster.width()
            h = self.Player_Battle_Monster.height()
            pixmap = QPixmap(self.manager.player.deck.battlePokemon.img).scaled(w, h, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            self.Player_Battle_Monster.setPixmap(pixmap)
            self.Player_Battle_Monster.setScaledContents(True)
            self.Player_Battle_Monster.setAlignment(Qt.AlignCenter)
            self.Player_Battle_Monster.setStyleSheet("border: 1px solid black;")

        if self.manager.ai.deck.battlePokemon:
            w = self.Ai_Battle_Monster.width()
            h = self.Ai_Battle_Monster.height()
            pixmap = QPixmap(self.manager.ai.deck.battlePokemon.img).scaled(w, h, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            self.Ai_Battle_Monster.setPixmap(pixmap)
            self.Ai_Battle_Monster.setScaledContents(True)
            self.Ai_Battle_Monster.setAlignment(Qt.AlignCenter)
            self.Ai_Battle_Monster.setStyleSheet("border: 1px solid black;")

        self.clear_layout(self.playerBench)
        for card in self.manager.player.deck.BenchPokemons:
            label = QLabel()
            label.setFixedSize(80, 120)
            pixmap = QPixmap(card.img).scaled(80, 120, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            label.setPixmap(pixmap)
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("border: 1px solid black;")
            self.playerBench.addWidget(label)

        self.clear_layout(self.aiBench)
        for card in self.manager.ai.deck.BenchPokemons:
            label = QLabel()
            label.setFixedSize(80, 120)
            pixmap = QPixmap(card.img).scaled(80, 120, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            label.setPixmap(pixmap)
            label.setAlignment(Qt.AlignCenter)
            label.setStyleSheet("border: 1px solid black;")
            self.aiBench.addWidget(label)

    def update_export_button_visibility(self):
        phase = self.manager.phase
        self.Export_Button.setEnabled(phase in ["game_ready", "export_card"])

    def setConsole(self):
        self.consoleLog.setReadOnly(True)
        self.consoleLog.setAlignment(Qt.AlignCenter)
        self.consoleLog.append("########## Monster Card Game #########")
        self.consoleLog.setAlignment(Qt.AlignLeft)
        self.consoleLog.append(">> Game Start...")

    def update_attack_retreat_buttons(self):
        self.clear_button_area()
        player = self.manager.player
        mon = player.deck.battlePokemon
        canAttack = mon.currentEnergy >= mon.skill_a_cost
        canRetreat = mon.currentEnergy >= mon.comeback and len(player.deck.BenchPokemons) > 0
        # 공격 버튼 조건
        if canAttack:
            attack_btn = QPushButton("공격")
            attack_btn.clicked.connect(self.show_attack_buttons)
            self.button_area_layout.addWidget(attack_btn)

        # 후퇴 버튼 조건
        if canRetreat:
            retreat_btn = QPushButton("후퇴")
            retreat_btn.clicked.connect(self.show_retreat_options)
            self.button_area_layout.addWidget(retreat_btn)

        if not canAttack and not canRetreat:
            self.consoleLog.append(">> 에너지가 부족해 아무 행동도 할 수 없습니다. 턴을 종료합니다.")
            self.manager.end_turn()

    def show_attack_buttons(self):
        self.clear_button_area()
        player_mon = self.manager.player.deck.battlePokemon

        if player_mon and player_mon.currentEnergy >= player_mon.skill_a_cost:
            btn1 = QPushButton("기술1")
            btn1.clicked.connect(lambda: self.manager.player.attack("a"))
            self.button_area_layout.addWidget(btn1)

        if hasattr(player_mon, "skill_b") and player_mon.currentEnergy >= player_mon.skill_b_cost:
            btn2 = QPushButton("기술2")
            btn2.clicked.connect(lambda: self.manager.player.attack("b"))
            self.button_area_layout.addWidget(btn2)

    def show_retreat_options(self):
        self.clear_button_area()
        for idx, bench_pokemon in enumerate(self.manager.player.deck.BenchPokemons):
            btn = QPushButton(f"{bench_pokemon.name}와 교체")
            btn.clicked.connect(lambda _, i=idx: self.manager.player.retreat(i))
            self.button_area_layout.addWidget(btn)
