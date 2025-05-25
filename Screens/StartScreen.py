import random
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from Deck import *

startForm= uic.loadUiType("ui/first.ui")[0]
class StartScreen(QMainWindow, startForm):
    def __init__(self,manager):
        super().__init__()
        self.setupUi(self)
        self.manager = manager
        self.chooseCharmander.clicked.connect(lambda: self.choose_pokemon("파이리"))
        self.chooseBulbasaur.clicked.connect(lambda:self.choose_pokemon("이상해씨"))
        self.chooseSquirtle.clicked.connect(lambda:self.choose_pokemon("꼬부기"))
        self.set_image_on_titleText()

    def choose_pokemon(self,pokemon):
        startinglist = ["파이리","이상해씨","꼬부기"]
        self.manager.player.deck = Deck(pokemon)
        remaining_pokemon = [p for p in startinglist if p != pokemon]
        self.manager.ai.deck =Deck((random.choice(remaining_pokemon)))
        self.manager.changeBattleScreen()
        print(self.manager.player.deck.drawCards)

    def set_image_on_titleText(self):
        # QLabel에 이미지 삽입
        pixmap1 = QPixmap("images/mainBackgroundImg.pngg")  # 이미지 파일 경로
        self.titleText.setPixmap(pixmap1)
        self.titleText.setScaledContents(True)  # 라벨 크기에 맞게 이미지를 조정