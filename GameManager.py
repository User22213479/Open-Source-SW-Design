from Screens.StartScreen import *
from Screens.BattleScreen import *
from Ai import Ai
from Player import Player
from Cards.Card import PokemonCard
import time
import threading

class GameManger:
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

        def wait_for_player_ready():
            # 기본 몬스터가 1장도 없으면 계속 대기
            while not self.has_player_basic_monster():
                time.sleep(1)

            self.battlescreen.consoleLog.append(">> 기본 몬스터가 배치되었습니다. 10초 안에 더 배치할 수 있습니다.")
            countdown = 10
            last_battle = self.player.deck.battlePokemon
            last_bench = list(self.player.deck.BenchPokemons)

            while countdown > 0:
                time.sleep(1)
                new_battle = self.player.deck.battlePokemon
                new_bench = list(self.player.deck.BenchPokemons)

                if new_battle != last_battle or len(new_bench) > len(last_bench):
                    self.battlescreen.consoleLog.append(">> 몬스터 추가 배치 감지. 10초를 다시 셉니다.")
                    countdown = 10
                    last_battle = new_battle
                    last_bench = new_bench
                else:
                    countdown -= 1

            self.battlescreen.consoleLog.append(">> 준비가 완료되었습니다. 게임을 시작합니다.")
            self.startGame()

        threading.Thread(target=wait_for_player_ready, daemon=True).start()

    def has_player_basic_monster(self):
        return self.player.deck.battlePokemon is not None

    def startGame(self):
        self.battlescreen.consoleLog.append(">> 동전을 던져 차례를 정합니다...")

gamemanager = GameManger()