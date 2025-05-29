from Screens.StartScreen import *
from Screens.BattleScreen import *
from Ai import Ai
from Player import Player
from Cards.Card import PokemonCard
from PyQt5.QtCore import QTimer
import time
import threading
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
        self.gameReady()  # 게임 준비 시작

    def player_turn(self):
        self.battlescreen.consoleLog.append(">> 당신의 차례입니다.")
        self.player.support_used_this_turn = False  # 턴 시작 초기화
        self.player.turn_counter += 1
        self.player.attach_energy()  # 첫 단계: 에너지 부착

    def ai_turn(self):
        self.battlescreen.consoleLog.append(">> AI의 차례입니다.")
        self.ai.support_used_this_turn = False  # 턴 시작 초기화
        self.ai.turn_counter += 1
        self.ai.attach_energy()  # 첫 단계: 에너지 부착

    def gameReady(self):
        self.battlescreen.consoleLog.append(">> 게임 준비 중입니다.")
        self.battlescreen.consoleLog.append(">> 기본 몬스터를 1장 이상 필드에 내보내 주세요.")

        # AI 기본 몬스터 자동 배치
        ai_cards = self.ai.deck.drawCards[:]
        for card in ai_cards:
            if isinstance(card, PokemonCard) and card.is_default:
                if self.ai.export_card(card):
                    self.ai.deck.drawCards.remove(card)

        self.battlescreen.consoleLog.append(">> AI는 몬스터를 배치했습니다.")

        self.wait_countdown = 3
        self.last_battle = self.player.deck.battlePokemon
        self.last_bench = list(self.player.deck.BenchPokemons)

        def check_player_ready():
            if not self.has_player_basic_monster():
                # 아직 몬스터 안 냈으면 다시 검사 예약
                QTimer.singleShot(1000, check_player_ready)
                return

            new_battle = self.player.deck.battlePokemon
            new_bench = list(self.player.deck.BenchPokemons)

            if new_battle != self.last_battle or len(new_bench) > len(self.last_bench):
                self.battlescreen.consoleLog.append(">> 몬스터 추가 배치 감지. 3초를 다시 셉니다.")
                self.wait_countdown = 3
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

        # 점수 초기화
        self.player_score = 0
        self.ai_score = 0

        # 동전 던지기로 선공자 결정
        #self.current_turn = random.choice(['player', 'ai'])

        self.current_turn = 'player'

        if self.current_turn == 'player':
            self.battlescreen.consoleLog.append(">> 당신이 선공입니다!")
        else:
            self.battlescreen.consoleLog.append(">> AI가 선공입니다!")

        self.game_loop()

    def game_loop(self):
        # 승리 조건 1: 점수
        if self.player_score >= 3:
            self.battlescreen.consoleLog.append(">> 당신이 승리했습니다! 🎉")
            return
        elif self.ai_score >= 3:
            self.battlescreen.consoleLog.append(">> AI가 승리했습니다. 😢")
            return

        # 승리 조건 2: 필드에 몬스터 없음
        if (not self.ai.deck.battlePokemon and not self.ai.deck.BenchPokemons):
            self.battlescreen.consoleLog.append(">> AI의 몬스터가 모두 쓰러졌습니다. 당신의 승리입니다! 🎉")
            return
        elif (not self.player.deck.battlePokemon and not self.player.deck.BenchPokemons):
            self.battlescreen.consoleLog.append(">> 당신의 몬스터가 모두 쓰러졌습니다. AI의 승리입니다! 😢")
            return

        # 턴 실행
        if self.current_turn == 'player':
            self.player_turn()
        else:
            self.ai_turn()

    def end_turn(self):
        self.current_turn = 'ai' if self.current_turn == 'player' else 'player'
        self.game_loop()

gamemanager = GameManager()
