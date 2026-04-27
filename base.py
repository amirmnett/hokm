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

class dast:
    def __init__(self):
        """با ساخت میز خودکار تمام کارت ها ساخته میشه"""
        self.list_kart = []       # list-e hame kart ha
        self._create_dast()       # seda zadan sakhte kart ha

    def _create_dast(self):
        """ساخت میز(54کارت)"""

        # Khal-ha 
        list_khal = ["Hearts", "Diamonds", "Clubs", "Spades"]

        # اسم هر کارت و امتیاز مربوط به آن
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

        # ساخت52 کارت
            for khal in list_khal:
            for ragham, emtiaz in ragham_emtiaz.items():
                self.list_kart.append(Card(khal, ragham, emtiaz))
    
        # ساخت 2 جوکر
        
        self.list_kart.append(Card(None, "Joker-Red", None))
        self.list_kart.append(Card(None, "Joker-Black", None))

    def bor(self):
        """بور زدن رندوم میز"""
        import random
        random.shuffle(self.list_kart)

    def bardasht_kart(self):
        """برداشتن بالا ترین کارت از دست """
        if len(self.list_kart) == 0:
            return None
        return self.list_kart.pop()

    def tedad_kart(self):
        """مقدار باقی مانده کارتها"""
        return len(self.list_kart)

    def namayesh(self):
        """Namayesh deck"""
        return self.list_kart


# ================================================
#  Example Usage
# ================================================

deck = dast()
deck.bar_zadan()

print("Tedad kart:", dast.tedad_kart())
print("Kart bardashte shode:", dast.bardasht_kart())
print("Baghimande:", dast.tedad_kart())
