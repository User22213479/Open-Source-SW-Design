from Screens.StartScreen import *
from Screens.BattleScreen import *
from Ai import Ai
from Player import Player
from Cards.Card import PokemonCard
from PyQt5.QtCore import QTimer
import sys
import random

class GameManager:
    def __init__(self):
        self.player = Player()
        self.ai = Ai()
        self.player.set_manager(self)
        self.ai.set_manager(self)
        self.InitialSetting()

    def InitialSetting(self):
        self.app = QApplication(sys.argv)
        self.startScreen = StartScreen(self)
        self.startScreen.show()
        self.app.exec_()

    def changeBattleScreen(self):
        self.battlescreen = BattleScreen(self)
        self.battlescreen.show()
        self.startScreen.close()
        self.gameReady()

    def player_turn(self):
        self.battlescreen.consoleLog.append(">> 당신의 차례입니다.")
        self.player.support_used_this_turn = False
        self.player.turn_counter += 1
        self.set_phase("attach_energy")
        self.player.attach_energy()

    def ai_turn(self):
        self.battlescreen.consoleLog.append(">> AI의 차례입니다.")
        self.ai.support_used_this_turn = False
        self.ai.turn_counter += 1
        self.set_phase("attach_energy")
        self.ai.attach_energy()
        self.set_phase("export_card")
        self.ai_export_card_phase()

    def ai_export_card_phase(self):
        cards_played = 0

        for card in self.ai.deck.drawCards[:]:  # 복사본 순회
            if self.ai.export_card(card):
                self.ai.deck.drawCards.remove(card)
                cards_played += 1
                if cards_played >= 2:
                    break  # 최대 2장까지만

        self.battlescreen.update_field_display()

        if cards_played == 0:
            self.battlescreen.consoleLog.append(">> AI는 낼 수 있는 카드가 없어 아무 것도 내지 않았습니다.")
        else:
            self.battlescreen.consoleLog.append(f">> AI가 {cards_played}장의 카드를 내보냈습니다.")

        self.set_phase("action_phase")
        self.battlescreen.consoleLog.append(">> AI의 공격/후퇴 단계입니다.")
        self.prepare_attack_or_retreat()

    def set_phase(self, phase_name):
        self.phase = phase_name
        if hasattr(self, 'battlescreen'):
            self.battlescreen.update_export_button_visibility()

        if self.phase == "export_card" and self.current_turn == "player":
            self.battlescreen.consoleLog.append(">> 카드를 내보낼 수 있습니다. (카드 내보낼 때 마다 5초 카운트)")
            self.export_timer_count = 5
            self.start_export_phase_timer()

    def start_export_phase_timer(self):
        def tick():
            if self.phase != "export_card":
                return
            self.export_timer_count -= 1
            if self.export_timer_count <= 0:
                self.battlescreen.consoleLog.append(">> 카드 내보내기 단계 종료. 다음 단계로 넘어갑니다.")
                self.set_phase("action_phase")
                self.prepare_attack_or_retreat()
            else:
                QTimer.singleShot(1000, tick)
        QTimer.singleShot(1000, tick)

    def restart_export_timer(self):
        self.export_timer_count = 5

    def prepare_attack_or_retreat(self):
        self.battlescreen.consoleLog.append(">> 다음 단계로 넘어갔습니다. 공격 혹은 후퇴를 선택하세요.")
        self.battlescreen.clear_button_area()
        # 공격/후퇴 버튼 구성은 이후 구현

    def gameReady(self):
        self.battlescreen.consoleLog.append(">> 게임 준비 중입니다.")
        self.battlescreen.consoleLog.append(">> 기본 몬스터를 1장 이상 필드에 내보내 주세요.")

        ai_cards = self.ai.deck.drawCards[:]
        for card in ai_cards:
            if isinstance(card, PokemonCard) and card.is_default:
                if self.ai.export_card(card):
                    self.ai.deck.drawCards.remove(card)

        self.battlescreen.consoleLog.append(">> AI는 몬스터를 배치했습니다.")

        self.phase = "game_ready"
        self.battlescreen.update_export_button_visibility()

        self.wait_countdown = 5
        self.last_battle = self.player.deck.battlePokemon
        self.last_bench = list(self.player.deck.BenchPokemons)

        def check_player_ready():
            if not self.has_player_basic_monster():
                QTimer.singleShot(1000, check_player_ready)
                return

            new_battle = self.player.deck.battlePokemon
            new_bench = list(self.player.deck.BenchPokemons)

            if new_battle != self.last_battle or len(new_bench) > len(self.last_bench):
                self.battlescreen.consoleLog.append(">> 몬스터 추가 배치 감지. 5초를 다시 셉니다.")
                self.wait_countdown = 5
                self.last_battle = new_battle
                self.last_bench = new_bench
            else:
                self.wait_countdown -= 1

            if self.wait_countdown <= 0:
                self.battlescreen.consoleLog.append(">> 준비가 완료되었습니다. 게임을 시작합니다.")
                self.startGame()
            else:
                QTimer.singleShot(1000, check_player_ready)

        QTimer.singleShot(1000, check_player_ready)

    def has_player_basic_monster(self):
        return self.player.deck.battlePokemon is not None

    def startGame(self):
        self.battlescreen.consoleLog.append(">> 동전을 던져 선공을 결정합니다...")
        self.player_score = 0
        self.ai_score = 0
        self.current_turn = 'ai'
        #self.current_turn = random.choice(['player', 'ai'])

        if self.current_turn == 'player':
            self.battlescreen.consoleLog.append(">> 당신이 선공입니다!")
        else:
            self.battlescreen.consoleLog.append(">> AI가 선공입니다!")

        self.game_loop()

    def game_loop(self):
        if self.player_score >= 3:
            self.battlescreen.consoleLog.append(">> 당신이 승리했습니다! 🎉")
            return
        elif self.ai_score >= 3:
            self.battlescreen.consoleLog.append(">> AI가 승리했습니다. 😢")
            return

        if (not self.ai.deck.battlePokemon and not self.ai.deck.BenchPokemons):
            self.battlescreen.consoleLog.append(">> AI의 몬스터가 모두 쓰러졌습니다. 당신의 승리입니다! 🎉")
            return
        elif (not self.player.deck.battlePokemon and not self.player.deck.BenchPokemons):
            self.battlescreen.consoleLog.append(">> 당신의 몬스터가 모두 쓰러졌습니다. AI의 승리입니다! 😢")
            return

        if self.current_turn == 'player':
            self.player_turn()
        else:
            self.ai_turn()

    def end_turn(self):
        self.current_turn = 'ai' if self.current_turn == 'player' else 'player'
        self.game_loop()

gamemanager = GameManager()
