import random

from samostalnavj7Error import samostalnavj7Error 


class samostalnavj7:
    def __init__(self):
        self.SPIL = {'2': 2, '3': 3, '4': 4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':10,
                      'Decko':10, 'Dama':10, 'Kralj':10, 'Kec':1}

    def display_title_bar(self):
        print("\t***************************************************")
        print("\t*** Kartaška igra - Razvoj poslovnih aplikacija ***")
        print("\t***************************************************")

    def get_user_choice(self):
        print("\n [1] Igraj Kartašku igru.")
        print("[x] Izlaz.")
        return input("Odaberite što želite napraviti?")

    def start_game(self):
        deck = (['2', '3', '4', '5', '6', '7', '8', '9', '0', 'Decko', 'Dama', 'Kralj', 'Kec'])*4 # puta 4 je zato što ima četiri boje u decku/kutiji karata
        random.shuffle(deck)
        self.score_igrac = 0
        self.score_racunalo = 0
        self.runda = 0

        while self.runda <= 2: 
            prva_karta = random.randint(1,10)
            druga_karta = random.randint(1,10)
            treca_karta = random.randint(1,10)
            cetvrta_karta = random.randint(1,10)
            zbroj_igrac = prva_karta + druga_karta        
            zbroj_racunalo = treca_karta + cetvrta_karta

            if zbroj_igrac > zbroj_racunalo:
                print("Igrač pobjeđuje. Zbroj karata igrača je {} vs. zbroj karata računala je {}".format(zbroj_igrac, zbroj_racunalo))
                self.score_igrac = self.score_igrac + 1
                print("Rezultat je Vi  {} vs. Računalo {}".format(self.score_igrac, self.score_racunalo))
            elif zbroj_igrac < zbroj_racunalo:
                print("Računalo pobjeđuje. Zbroj karata računala je {} vs. zbroj karata igrača {}".format(zbroj_racunalo, zbroj_igrac))
                self.score_racunalo = self.score_racunalo + 1
                print("Rezultat je Računalo  {} vs. Vi {}".format(self.score_racunalo, self.score_igrac))
            else:
                print("Zbroj Vaših karata i karata Računala je izjednačen!")
            self.runda = self.runda + 1

        if self.score_igrac > self.score_racunalo:
            print("Kraj igre. Vi ste pobjedili. Čestitamo. Rezultat je Vi {} vs Računalo {}".format(self.score_igrac, self.score_racunalo))
        elif self.score_racunalo > self.score_igrac:
            print("Kraj igre. Izgubili ste. Pobjednik je Računalo. Rezultat je Računalo {} vs. Vi {}".format(self.score_racunalo, self.score_igrac))
        else:
            print("Nema pobjednika! Zbroj Vaših karata i karata Računala je izjednačen!")
            
    def play(self):
        choice = ''
        self.display_title_bar()
        while choice != 'x':
            choice = self.get_user_choice()
            self.display_title_bar()
            if choice == '1':
                self.start_game()
            elif choice == 'x':
                print("Hvala na igranju. Pozdrav!")
            else:
                raise igraError(101)
    
if __name__ == '__main__':
    game = samostalnavj7()
    game.play()