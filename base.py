# ================================================
#  Class: Card
#  -> Tarif yek kart ba khal, raghame_kart va emtiaz
# ================================================

class Card:
    def __init__(self, khal, ragham, emtiaz):
        """
        khal   : str | None   -> Hearts, Diamonds, Clubs, Spades | None baraye Joker
        ragham : str          -> A, K, Q, J, ... ya esm-e Joker
        emtiaz : int          -> arzesh kart
        """

        self.khal = khal          # khal-e kart (mesl Hearts)
        self.ragham = ragham      # raghame kart (mesl A, K, Q...)
        self.emtiaz = emtiaz      # emtiaze kart (baraye moghayese)

    def __repr__(self):
        """Chap kardane kart be soorate ghabl-e khavan"""
        if self.khal is None:  
            return f"{self.ragham}"    # Joker
        return f"{self.ragham} of {self.khal}"


# ================================================
#  Class: Deck
#  -> Tarif yek deck kamel (54 kart)
# ================================================

class Deck:
    def __init__(self):
        """Dar sakhte deck be soorate khodkar tamame kart-ha sakhte mishavand."""
        self.list_kart = []       # list-e hame kart ha
        self._create_deck()       # seda zadan sakhte kart ha

    def _create_deck(self):
        """Sakhtane deck (52 kart asli + 2 Joker)"""

        # Khal-ha (finglish)
        list_khal = ["Hearts", "Diamonds", "Clubs", "Spades"]

        # Raghame kart + emtiaz-ha
        ragham_emtiaz = {
            "A": 14,
            "K": 13,
            "Q": 12,
            "J": 11,
            "10": 10,
            "9": 9,
            "8": 8,
            "7": 7,
            "6": 6,
            "5": 5,
            "4": 4,
            "3": 3,
            "2": 2
        }

        # -------------------------------------
        # Sakhtane 52 kart
        # -------------------------------------
        for khal in list_khal:
            for ragham, emtiaz in ragham_emtiaz.items():
                self.list_kart.append(Card(khal, ragham, emtiaz))

        # -------------------------------------
        # Ezafe kardane 2 Joker
        # -------------------------------------
        self.list_kart.append(Card(None, "Joker-Red", 0))
        self.list_kart.append(Card(None, "Joker-Black", 0))

    def bar_zadan(self):
        """Bar zadan deck be soorate random"""
        import random
        random.shuffle(self.list_kart)

    def bardasht_kart(self):
        """Bardashtane bala-tarin kart az deck (pop)"""
        if len(self.list_kart) == 0:
            return None
        return self.list_kart.pop()

    def tedad_kart(self):
        """Bargasht dadan tedad kart haye baghi mande"""
        return len(self.list_kart)

    def namayesh(self):
        """Namayesh deck"""
        return self.list_kart


# ================================================
#  Example Usage
# ================================================

deck = Deck()
deck.bar_zadan()

print("Tedad kart:", deck.tedad_kart())
print("Kart bardashte shode:", deck.bardasht_kart())
print("Baghimande:", deck.tedad_kart())
