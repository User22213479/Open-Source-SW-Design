from Cards.FireType import Charmander, Charmeleon, Charizard, Ponyta, Rapidash, Salandit, Salazzle, Moltres
from Cards.GrassType import Bulbasaur, Exeggcute, Exeggutor, Skiddo, Gogoat, Ivysaur, Venusaur
from Cards.WaterType import Squirtle, Psyduck, Pyukumuku, Wartortle, Golduck, Lapras, Articuno, Blastoise
from Cards.NormalType import Rattata, Raticate
from Cards.Item import PokeBall, Potion
from Cards.Support import DoctorStudy, MinHwa, Isul
import Cards
import random

class Deck:
    def __init__(self, pokemon):
        # cards는 덱에 포함된 카드들의 리스트
        self.setDeck(pokemon)
        self.shuffle()
        self.drawCards = self.draw_multiple_cards(5)
        self.battlePokemon = None
        self.BenchPokemons= []

    def setDeck(self,pokemon):
        if pokemon == "파이리":
            self.cards = create_charizard_deck()
        elif pokemon == "이상해씨":
            self.cards = create_bulbasaur_deck()
        elif pokemon == "꼬부기":
            self.cards = create_squirtle_deck()

    def shuffle(self):
        """덱을 셔플합니다."""
        random.shuffle(self.cards)

    def draw_card(self):
        """덱에서 카드를 한 장 뽑습니다."""
        if self.cards:
            return self.cards.pop()

    def draw_multiple_cards(self, num):
        drawn_cards = []
        # 기본 포켓몬이 포함될 때까지 반복
        default_pokemon_found = False
        while not default_pokemon_found and len(drawn_cards) < num:
            drawn_cards = []
            # 카드를 뽑을 때 기본 포켓몬이 하나라도 포함되도록 한다
            for _ in range(num):
                card = self.draw_card()
                drawn_cards.append(card)

            # 기본 포켓몬이 있는지 확인
            default_pokemon_found = any(isinstance(card, Cards.Card.PokemonCard) and card.is_default for card in drawn_cards)

            # 기본 포켓몬이 없으면 덱에 다시 넣고 다시 뽑기
            if not default_pokemon_found:
                for card in drawn_cards:
                    self.cards.append(card)
                random.shuffle(self.cards)

        return drawn_cards

# 각 덱을 정의하는 예시
def create_charizard_deck():
    # 파이리 덱
    return [
        Charmander(), Charmander(), Ponyta(), Ponyta(),
        Salandit(), Salandit(), Salazzle(), Charmeleon(), Charmeleon(),
        Rapidash(), Moltres(), Charizard(), Rattata(), Rattata(),
        Raticate(), Potion(), PokeBall(), PokeBall(),
        DoctorStudy(), DoctorStudy()
    ]


def create_bulbasaur_deck():
    # 이상해씨 덱
    return [
        Bulbasaur(), Bulbasaur(), Exeggcute(), Exeggcute(),
        Skiddo(), Skiddo(), Gogoat(), Ivysaur(), Ivysaur(),
        Venusaur(), Exeggutor(), Rattata(), Rattata(),
        Raticate(), Potion(), PokeBall(), PokeBall(),
        DoctorStudy(), DoctorStudy()
    ]


def create_squirtle_deck():
    # 꼬부기 덱
    return [
        Squirtle(), Squirtle(), Psyduck(), Psyduck(),
        Pyukumuku(), Wartortle(), Wartortle(), Golduck(),
        Lapras(), Articuno(), Blastoise(), Rattata(), Rattata(),
        Raticate(), Potion(), PokeBall(), PokeBall(),
        DoctorStudy(), DoctorStudy()
    ]
